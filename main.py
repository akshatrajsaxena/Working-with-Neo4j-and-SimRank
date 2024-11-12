from pyspark.sql import SparkSession
import networkx as nx
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from itertools import product
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_graph_from_csv(filename):
    """Create a NetworkX directed graph from CSV file."""
    df = pd.read_csv(filename)
    G = nx.DiGraph()
    for _, row in df.iterrows():
        G.add_edge(str(row['source']), str(row['target']))
    return G

def batch_simrank_similarity(G, source=None, importance_factor=0.9, max_iterations=100, tolerance=0.0001, batch_size=1000):
    """Memory-efficient implementation of SimRank algorithm using batched processing."""
    nodes = list(G.nodes())
    n = len(nodes)
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    
    logger.info(f"Processing graph with {n} nodes")
    
    if source is not None:
        
        source_idx = node_to_idx[source]
        sim_curr = lil_matrix((n, 1), dtype=np.float64)
        sim_curr[source_idx, 0] = 1.0
        sim_prev = lil_matrix((n, 1), dtype=np.float64)
        
        for iteration in range(max_iterations):
            logger.info(f"Iteration {iteration + 1}/{max_iterations}")
            sim_prev = sim_curr.copy()
            sim_curr = lil_matrix((n, 1), dtype=np.float64)
            sim_curr[source_idx, 0] = 1.0
            
            
            for start_idx in range(0, n, batch_size):
                end_idx = min(start_idx + batch_size, n)
                batch_nodes = nodes[start_idx:end_idx]
                
                for v_node in batch_nodes:
                    v = node_to_idx[v_node]
                    if v == source_idx:
                        continue
                    
                    u_neighbors = list(G.predecessors(nodes[source_idx]))
                    v_neighbors = list(G.predecessors(v_node))
                    
                    if not u_neighbors or not v_neighbors:
                        sim_curr[v, 0] = 0
                        continue
                    
                    sum_sim = 0
                    for u_nbr, v_nbr in product(u_neighbors, v_neighbors):
                        u_nbr_idx = node_to_idx[u_nbr]
                        v_nbr_idx = node_to_idx[v_nbr]
                        sum_sim += sim_prev[v_nbr_idx, 0]
                    
                    sim_curr[v, 0] = (importance_factor * sum_sim) / (len(u_neighbors) * len(v_neighbors))
            
            
            if np.abs(sim_curr - sim_prev).max() < tolerance:
                logger.info(f"Converged after {iteration + 1} iterations")
                break
        
        return {nodes[i]: sim_curr[i, 0] for i in range(n)}
    
    else:
        raise ValueError("Full matrix computation not supported in memory-efficient version. Please specify a source node.")

def main():
    try:
        
        spark = SparkSession.builder \
            .appName("SimRank Analysis") \
            .getOrCreate()
        
        
        spark.sparkContext.setLogLevel("INFO")

        logger.info("Reading graph from CSV")
        G = create_graph_from_csv('export.csv')
        
        
        logger.info(f"Loaded graph with {len(G.nodes())} nodes and {len(G.edges())} edges")
        
        
        query_nodes = ['2982615777', '1556418098']
        c_values = [0.7, 0.8, 0.9]
        
        logger.info("Starting SimRank calculations")
        with open('simrank_result.txt', 'w') as f:
            for c in c_values:
                f.write(f"\nResults for C = {c}:\n")
                f.write("=" * 50 + "\n")
                
                for query_node in query_nodes:
                    if query_node not in G.nodes():
                        f.write(f"\nQuery node {query_node} not found in graph.\n")
                        continue
                        
                    f.write(f"\nSimilar nodes to {query_node}:\n")
                    f.write("-" * 30 + "\n")
                    
                    
                    logger.info(f"Calculating similarities for query node {query_node} with C={c}")
                    similarities = batch_simrank_similarity(G, source=query_node, importance_factor=c)
                    
                    
                    sorted_nodes = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
                    
                    
                    for node, sim in sorted_nodes[:10]:
                        if node != query_node:  
                            f.write(f"Node: {node}, Similarity: {sim:.4f}\n")
        
        logger.info("SimRank analysis completed")
        spark.stop()
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()