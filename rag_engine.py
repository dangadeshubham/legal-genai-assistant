import re
from pypdf import PdfReader

PDF_PATH = "data/constitution.pdf"
MAX_CHARS = 700  # strict limit to avoid dumping text


def load_pdf_text():
    reader = PdfReader(PDF_PATH)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += "\n" + page_text
    return text


PDF_TEXT = load_pdf_text()


def extract_article(article_number: str):
    """
    Robust extractor for Indian Constitution articles.
    Handles:
    - 21.
    - 21A.
    - Article number anywhere in line
    """

    # Find all article starts like: 21., 21A., 300A.
    article_positions = [
        (m.start(), m.group())
        for m in re.finditer(r"\b\d+[A-Z]?\s*[.\-—]\s+", PDF_TEXT)
    ]

    start_index = None
    end_index = None

    for i, (pos, label) in enumerate(article_positions):
        if label.strip().startswith(article_number):
            start_index = pos
            if i + 1 < len(article_positions):
                end_index = article_positions[i + 1][0]
            break

    if start_index is None:
        return None

    article_text = PDF_TEXT[start_index:end_index]

    # Remove sub-articles like 21A if user asked only 21
    article_text = re.split(rf"\b{article_number}[A-Z]\s*[.\-—]\s+", article_text)[0]

    # Clean whitespace
    article_text = re.sub(r"\s+", " ", article_text).strip()

    return article_text[:MAX_CHARS]
