from app.retrieval.embedder import Embedder
from app.retrieval.vector_store import VectorStore


def test_vector_store():
    embedder = Embedder()

    chunks = [
        {
            "chunk_id": 0,
            "page": 1,
            "text": "MariaDB 主機名稱與資料庫伺服器設定方式。",
        },
        {
            "chunk_id": 1,
            "page": 2,
            "text": "Python 可以使用 FastAPI 建立 Web API。",
        },
        {
            "chunk_id": 2,
            "page": 3,
            "text": "今天的天氣很好，適合出去散步。",
        },
    ]

    texts = [chunk["text"] for chunk in chunks]

    embeddings = embedder.encode(texts)

    vector_store = VectorStore(
        dimension=embeddings.shape[1]
    )

    vector_store.add(
        embeddings,
        chunks,
    )

    query = "資料庫主機名稱要怎麼設定？"

    query_embedding = embedder.encode([query])[0]

    results = vector_store.search(
        query_embedding,
        top_k=2,
    )

    assert len(results) == 2
    assert results[0]["chunk_id"] == 0

    for result in results:
        print(
            f"Score: {result['score']:.4f} | "
            f"Page: {result['page']} | "
            f"Text: {result['text']}"
        )