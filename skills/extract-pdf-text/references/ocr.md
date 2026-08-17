# OCR Setup — Extract PDF Text

## When to Use OCR

PyMuPDF extracts embedded text instantly. OCR is only needed for:
- Scanned documents (images of pages)
- PDFs where text is actually an image
- Very old PDFs with non-standard encoding

## Install the OCR dependencies

Install the Tesseract executable with the host package manager, then install the Python bindings in the active environment:

```bash
# macOS
brew install tesseract

# Ubuntu/Debian
sudo apt install tesseract-ocr

# Python packages
python3 -m pip install pytesseract Pillow
```

Confirm the executable is reachable before running OCR:

```bash
tesseract --version
```

## OCR with PyMuPDF + Tesseract

```python
import fitz
import pytesseract
from PIL import Image
import io

def ocr_page(page, lang="eng"):
    """OCR a single page using Tesseract."""
    # Render page to image
    pix = page.get_pixmap(dpi=300)
    img = Image.open(io.BytesIO(pix.tobytes()))
    
    # Run OCR
    text = pytesseract.image_to_string(img, lang=lang)
    return text

# Usage
doc = fitz.open("scanned.pdf")
for page in doc:
    text = ocr_page(page, lang="eng")
    print(text)
```

## Route each page: native text first, OCR only when needed

```python
def extract_smart(pdf_path, ocr_lang="eng"):
    """Extract text, using OCR only when needed."""
    doc = fitz.open(pdf_path)
    results = []
    
    for page in doc:
        text = page.get_text().strip()
        
        if len(text) >= 50:
            # Has enough native text; OCR is unnecessary
            results.append({"text": text, "method": "native"})
        else:
            # Likely scanned, use OCR
            ocr_text = ocr_page(page, ocr_lang)
            results.append({"text": ocr_text, "method": "ocr"})
    
    doc.close()
    return results
```

## Language Codes

| Language | Code |
|----------|------|
| English | `eng` |
| Spanish | `spa` |
| French | `fra` |
| German | `deu` |
| Chinese | `chi_sim` |

**Multiple languages:**
```python
text = pytesseract.image_to_string(img, lang="eng+spa")
```

## Verify and improve OCR quality

1. Render at **at least 300 DPI**; lower-resolution images commonly reduce recognition accuracy.
2. Pass the appropriate Tesseract language code, such as `eng` or `chi_sim`; install the corresponding language data before relying on it.
3. Compare OCR text with the page image. If it is unreliable, inspect orientation, skew, contrast, noise, borders, and page-segmentation mode before retrying.
4. For a small region, set a suitable Tesseract page-segmentation mode, for example `config="--psm 6"` for a uniform text block. Verify the selected mode against the input layout.

For known Tesseract preprocessing limits and recovery options, see https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html.
