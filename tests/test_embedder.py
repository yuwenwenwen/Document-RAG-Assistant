from app.retrieval.embedder import Embedder
from sentence_transformers.util import cos_sim


def test_embedder():
    embedder = Embedder()

    texts = [
        "MariaDB 主機名稱怎麼修改？",
        "如何設定資料庫伺服器名稱？",
        "今天天氣很好。",
    ]

    embeddings = embedder.encode(texts)

    assert len(embeddings) == 3
    assert len(embeddings[0]) > 0

    similarity_ab = cos_sim(
        embeddings[0],
        embeddings[1],
    ).item()

    similarity_ac = cos_sim(
        embeddings[0],
        embeddings[2],
    ).item()

    print("Embedding shape:", embeddings.shape)
    print(f"A ↔ B similarity: {similarity_ab:.4f}")
    print(f"A ↔ C similarity: {similarity_ac:.4f}")

    assert similarity_ab > similarity_ac