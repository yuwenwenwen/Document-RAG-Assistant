def chunk_text(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[str]:

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    text = text.strip()

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # 已經讀到文件最後面 跳出while
        if end == len(text):
            break

        start += chunk_size - overlap

    return chunks


def chunk_document(
    pages: list[dict],
    chunk_size: int = 1000,
    overlap: int = 200,
) -> list[dict]:

    chunks = []
    chunk_id = 0

    for page in pages:
        page_chunks = chunk_text(
            page["text"],
            chunk_size=chunk_size,
            overlap=overlap,
        )

        for text in page_chunks:
            chunks.append({
                "chunk_id": chunk_id,
                "page": page["page"],
                "text": text,
            })

            chunk_id += 1

    return chunks