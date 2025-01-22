### Note: Running Neo4j Docker Container

```bash
    # Run neo4j on docker
    docker pull neo4j

    docker run --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data neo4j

    # Delete all nodes and relationships in neo4j
    MATCH (n)
    DETACH DELETE n
```

### Reference

- https://towardsdatascience.com/enterprise-ready-knowledge-graphs-96028d863e8c
- https://github.com/langchain-ai/langchain/issues/12901
