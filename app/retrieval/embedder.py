from sentence_transformers import SentenceTransformer

# sentence embedding model: all-MiniLM-L6-v2 
class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list[str]):
        return self.model.encode(texts)