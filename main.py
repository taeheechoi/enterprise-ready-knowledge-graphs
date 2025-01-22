import os

from langchain_neo4j import GraphCypherQAChain, Neo4jGraph
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_experimental.graph_transformers import LLMGraphTransformer

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URL"),
    username=os.getenv("NEO4J_USERNAME", "neo4j"),
    password=os.getenv("NEO4J_PASSWORD"),
)
llm = llm = AzureChatOpenAI(
    azure_deployment="gpt-4o",
    # model="gpt-4o",  # must append 'azure/' in order to call azure llm in Crew lib.
    api_version="2024-08-01-preview",
    temperature=0,
)
# ------------------- Important --------------------
# llm_transformer = LLMGraphTransformer(llm)

llm_transformer = LLMGraphTransformer(
    llm=llm,
    allowed_nodes=["Person", "Company", "University"],
    allowed_relationships=[
        ("Person", "CEO_OF", "Company"),
        ("Person", "CFO_OF", "Company"),
        ("Person", "CTO_OF", "Company"),
        ("Person", "STUDIED_AT", "University"),
    ],
    node_properties=True,
)
# ------------------- Important --------------------

document = TextLoader("data/sample.txt").load()

graph_documents = llm_transformer.convert_to_graph_documents(document)

graph.add_graph_documents(graph_documents)
