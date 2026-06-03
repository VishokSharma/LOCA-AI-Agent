from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)


class QdrantManager:

    COLLECTION_NAME = "knowledge_base"
    VECTOR_SIZE = 768

    def __init__(self):

        self.client = QdrantClient(
            path="./data/qdrant"
        )

        self.create_collection()
        
    def close(self):
        self.client.close()
        
    def create_collection(self):
