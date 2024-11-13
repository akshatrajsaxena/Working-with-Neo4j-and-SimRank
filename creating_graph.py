from neo4j import GraphDatabase
import json
uri = "bolt:
username = " neo4j "  
password = " akshat @raj123 "  


data = []
with open(" C: / Users / raksh /.Neo4jDesktop / relate - data / dbmss / dbms - 29266b92-f6de-49be-87ed-2a6e4803870e / import / train.json ", " r ") as f:
    for line in f:
        data.append(json.loads(line))


driver = GraphDatabase.driver(uri, auth=(username, password))


def create_citation_graph(tx, paper_id, venue, text, references):
    
    tx.run(""" MERGE (p :Paper { id: $paper_id })
SET p.venue = $venue,
    p.text = $text """, paper_id=paper_id, venue=venue, text=text)

    
    for ref_id in references:
        tx.run(""" MERGE (ref :Paper { id: $ref_id }) MERGE (p :Paper { id: $paper_id }) - [:CITES]->(ref) """, paper_id=paper_id, ref_id=ref_id)


def insert_data(data):
    with driver.session() as session:
        for entry in data:
            paper_id = entry.get(" paper ")
            venue = entry.get(" venue ")
            text = entry.get(" text ")
            references = entry.get(" reference ", [])
            session.write_transaction(create_citation_graph, paper_id, venue, text, references)


insert_data(data)

# The Below is for verifying the graph in Neo4j
# MATCH (p:Paper)-[:CITES]->(ref:Paper)
# RETURN p, ref


# Exporting the csv from Neo4j
# MATCH (p:Paper)-[:CITES]->(ref:Paper)
# RETURN p.id AS source, ref.id AS target
