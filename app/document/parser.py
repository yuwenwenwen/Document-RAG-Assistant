import pymupdf

# PDF  binary data
def parse_pdf(content: bytes) -> list[dict]:
    # 從已經拿到的 bytes 開啟 PDF
    document = pymupdf.open(stream=content, filetype="pdf")

    pages = []

    # page numbers of pdf, json
    for page_number, page in enumerate(document):
        text = page.get_text()

        pages.append({
            "page": page_number + 1,
            "text": text,
        })

    document.close()

    return pages