import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        # Flat: 暴力精確搜尋，不使用近似搜尋。
        # IP: Inner Product
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, embeddings, chunks):
        embeddings = np.asarray(
            embeddings,
            dtype="float32",
        )

        # 正規化 length=1
        faiss.normalize_L2(embeddings)

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k: int = 3):
        query_embedding = np.asarray(
            [query_embedding],
            dtype="float32",
        )

        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(
            query_embedding,
            top_k,
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            results.append({
                "score": float(score),
                **self.chunks[index],
            })

        return results