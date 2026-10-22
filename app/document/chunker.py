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
    chunk_size: int = 500,
    overlap: int = 100,
) -> list[dict]:

    chunks = []
    chunk_id = 0

    for page in pages:
        page_chunks = chunk_by_lines(
            page["text"],
            chunk_size=chunk_size,
            overlap_lines=2,
        )

        for text in page_chunks:
            chunks.append({
                "chunk_id": chunk_id,
                "page": page["page"],
                "text": text,
            })

            chunk_id += 1

    return chunks

def chunk_by_lines(
    text: str,
    chunk_size: int = 1000,
    overlap_lines: int = 2,
) -> list[str]:

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return []

    chunks = []
    current_lines = []

    for line in lines:
        current_text = "\n".join(current_lines)

        if len(current_text) + len(line) + 1 <= chunk_size:
            current_lines.append(line)
            continue

        if current_lines:
            chunks.append("\n".join(current_lines))

            overlap = current_lines[-overlap_lines:]
            current_lines = overlap.copy()

        if len(line) > chunk_size:
            long_line_chunks = chunk_text(
                line,
                chunk_size=chunk_size,
                overlap=200,
            )

            chunks.extend(long_line_chunks)
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        chunks.append("\n".join(current_lines))

    return chunks