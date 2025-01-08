import PyPDF2
from docx import Document

def pdf_to_doc(input_pdf_path, output_doc_path):
    pdf = PyPDF2.PdfFileReader(input_pdf_path)
    doc = Document()

    for page_num in range(pdf.numPages):
        page = pdf.getPage(page_num)
        text = page.extractText()
        doc.add_paragraph(text)

        doc.save(output_doc_path)
        print(f"PDF successfully converted to Word document. Output saved at: {output_doc_path}")

        #Usage example:
        input_pdf_path = "path/to/input.pdf"
        output_doc_path = "path/to/output.docx"
        pdf_to_doc(input_pdf_path, output_doc_path)