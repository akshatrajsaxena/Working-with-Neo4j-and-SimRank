<h1 align="center">Working with Neo4j and SimRank</h1>
<p align="center"><i>Analyzing a citation graph using Neo4j and SimRank algorithm</i></p>
<div align="center">
  <a href="https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank/stargazers"><img src="https://img.shields.io/github/stars/akshatrajsaxena/Working-with-Neo4j-and-SimRank" alt="Stars Badge"/></a>
  <a href="https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank/network/members"><img src="https://img.shields.io/github/forks/akshatrajsaxena/Working-with-Neo4j-and-SimRank" alt="Forks Badge"/></a>
  <a href="https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank/pulls"><img src="https://img.shields.io/github/issues-pr/akshatrajsaxena/Working-with-Neo4j-and-SimRank" alt="Pull Requests Badge"/></a>
  <a href="https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank/issues"><img src="https://img.shields.io/github/issues/akshatrajsaxena/Working-with-Neo4j-and-SimRank" alt="Issues Badge"/></a>
  <a href="https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/akshatrajsaxena/Working-with-Neo4j-and-SimRank" ?color=2b9348"></a>
  <a href="https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank/blob/master/LICENSE"><img src="https://img.shields.io/github/license/akshatrajsaxena/Working-with-Neo4j-and-SimRank ?color=2b9348" alt="License Badge"/></a>
</div>
<br>

# Working with Neo4j and SimRank

This project focuses on analyzing a citation graph using Neo4j, a graph database, and the SimRank algorithm for finding similarities between research papers.

## Project Overview

The main objectives of this project are:

1. **Data Preprocessing for Neo4j**: The JSON dataset containing information about research papers, including their IDs, venues, text, and references, is preprocessed and converted into a format suitable for ingestion into Neo4j.

2. **Generating Citation Graph in Neo4j**: The preprocessed data is then used to create a directed citation graph in Neo4j, where each paper is represented as a node, and the citations between papers are represented as directed edges.

3. **Running SimRank Algorithm using Apache Spark**: The citation graph is then exported from Neo4j and analyzed using the SimRank algorithm, which is implemented in Python using Apache Spark. The SimRank algorithm computes the similarity between nodes (research papers) based on their citation patterns.

4. **Insights and Findings**: The project provides insights into the citation patterns and identifies the most similar research papers based on the SimRank analysis.

## Technologies Used

- **Neo4j**: A graph database used to store and manage the citation graph.
- **Apache Spark**: A distributed computing framework used to implement the memory-efficient version of the SimRank algorithm.
- **Python**: The primary programming language used for data preprocessing, graph creation, and SimRank algorithm implementation.
- **NetworkX**: A Python library used for working with the citation graph data.

## Getting Started

To get started with the project, please follow these steps:

### 1. **Clone the Repository**:

```
git clone https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank.git
```

### 2. **Install Dependencies**:

Ensure you have Python and the necessary packages installed, such as `pandas`, `networkx`, and `pyspark`.

```
pip install numpy
pip install  pandas
pip install  netwrkx
pip install pyspark
pip install scipy
```


### 3. **Set up Neo4j**:

Install and set up a Neo4j instance on your local machine or a remote server.

### 4. **Run the Data Preprocessing and Graph Creation**:

Execute the Python scripts to preprocess the JSON data, upload it to Neo4j, and export the citation graph to a CSV file.

### 5. **Run the SimRank Algorithm**:

Run the Python script that implements the SimRank algorithm using Apache Spark to analyze the citation graph.

### 6. **Analyze the Results**:

Review the output of the SimRank analysis, which includes the top-k most similar research papers for each query node.

## Project Structure

The project is organized into the following main components:

- `data_preprocessing.py`: Contains the code for preprocessing the JSON data and creating the Neo4j graph.
- `simrank.py`: Implements the memory-efficient version of the SimRank algorithm using Apache Spark.
- `output.png`: A sample output image showing the SimRank similarity results between selected papers.

## License

This project is licensed under the [MIT License](https://github.com/akshatrajsaxena/Working-with-Neo4j-and-SimRank/blob/main/LICENSE)

## Contact

If you have any questions or would like to get in touch, you can reach me at [Akshat Raj Saxena](mailto:akshat22054@iiitd.ac.in).
