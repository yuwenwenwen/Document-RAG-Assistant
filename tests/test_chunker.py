from app.document.chunker import chunk_text

def test_chunk_text():
    text = "A" * 2500
    # 切割
    chunks = chunk_text(
        text,
        chunk_size=1000,
        overlap=200,
    )

    # 檢查答案
    assert len(chunks) == 3

    assert len(chunks[0]) == 1000
    assert len(chunks[1]) == 1000
    assert len(chunks[2]) == 900

    assert chunks[0][-200:] == chunks[1][:200]

    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {len(chunk)} characters")