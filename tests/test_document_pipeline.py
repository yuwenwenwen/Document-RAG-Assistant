from app.document.parser import parse_pdf
from app.document.chunker import chunk_document


def test_document_pipeline():
    with open("test_data/sample.pdf", "rb") as file:
        content = file.read()

    pages = parse_pdf(content)

    chunks = chunk_document(
        pages,
        chunk_size=1000,
        overlap=200,
    )

    assert len(pages) > 0
    assert len(chunks) > 0

    for chunk in chunks:
        assert "chunk_id" in chunk
        assert "page" in chunk
        assert "text" in chunk

    print(f"Pages: {len(pages)}")
    print(f"Chunks: {len(chunks)}")

    for chunk in chunks:
        print(
            f"Chunk {chunk['chunk_id']} | "
            f"Page {chunk['page']} | "
            f"{len(chunk['text'])} characters"
        )