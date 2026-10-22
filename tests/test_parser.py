from app.document.parser import parse_pdf


def test_parse_pdf():
    # 用 binary 模式讀取 PDF
    with open("test_data/sample.pdf", "rb") as file:
        content = file.read()

    pages = parse_pdf(content)

    # 預期一定成立的條件
    assert len(pages) > 0
    assert pages[0]["page"] == 1
    assert "text" in pages[0]

    print(f"Pages: {len(pages)}")
    print(pages[0]["text"][:500])