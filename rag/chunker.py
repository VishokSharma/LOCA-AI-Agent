class Chunker:

    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100

    def __init__(self):
        pass

    def chunk_text(self, text):

        chunks = []

        start = 0

