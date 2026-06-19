from pathlib import Path
from uuid import uuid4

from rag.chunker import Chunker
from rag.embedder import Embedder
from rag.qdrant_manager import QdrantManager


class KnowledgeTool:

    def __init__(self):

        self.chunker = Chunker()
        self.embedder = Embedder()
        self.qdrant = QdrantManager()

    def add_document(self, path):

        try:

            path = Path(path)

            text = path.read_text(
                encoding="utf-8"
            )

            chunks = self.chunker.chunk_text(
                text
            )
            self.qdrant.delete_source(
            path.name
            )
            for chunk in chunks:
