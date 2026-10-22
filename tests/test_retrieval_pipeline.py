from app.document.parser import parse_pdf
from app.document.chunker import chunk_document
from app.retrieval.embedder import Embedder
from app.retrieval.vector_store import VectorStore


def test_retrieval_pipeline():
    # 1. Read PDF
    with open("test_data/sample.pdf", "rb") as file:
        content = file.read()

    # 2. Parse PDF
    pages = parse_pdf(content)

    # 3. Split document into chunks
    chunks = chunk_document(
        pages,
        chunk_size=1000,
        overlap=200,
    )

    # 4. Create embeddings
    embedder = Embedder()

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = embedder.encode(texts)

    # 5. Build vector index
    vector_store = VectorStore(
        dimension=embeddings.shape[1]
    )

    vector_store.add(
        embeddings,
        chunks,
    )

    # 6. User query
    query = "MariaDB 主機名稱怎麼修改？"

    query_embedding = embedder.encode([query])[0]

    # 7. Retrieve relevant chunks
    results = vector_store.search(
        query_embedding,
        top_k=3,
    )

    assert len(results) > 0

    print(f"\nQuery: {query}")
    print(f"Pages: {len(pages)}")
    print(f"Chunks: {len(chunks)}")

    print("\nRetrieved results:")

    for result in results:
        print("-" * 60)

        print(
            f"Score: {result['score']:.4f} | "
            f"Page: {result['page']} | "
            f"Chunk: {result['chunk_id']}"
        )

        print(result["text"][:500])