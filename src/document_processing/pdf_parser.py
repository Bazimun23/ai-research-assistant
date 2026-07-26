import fitz


class PDFProcessor:

    def extract_text(self, pdf_path):

        document = fitz.open(pdf_path)

        pages = []

        for page_number in range(len(document)):
            page = document[page_number]

            text = page.get_text("text")

            if text.strip():
                pages.append({
                    "page_number": page_number + 1,
                    "text": text.strip()
                })

        total_pages = len(document)

        document.close()

        return {
            "total_pages": total_pages,
            "pages": pages
        }