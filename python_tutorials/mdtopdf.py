from spire.doc import *
from spire.doc.common import *

# Create a Document object
document = Document()

# Load a Markdown file
document.LoadFromFile("string.md")

document.SaveToFile("output/ToWord.docx", FileFormat.Docx2016)

# Dispose resources
document.Dispose()
# import markdown
# import pdfkit

# # Read Markdown file
# with open('Basic.md', 'r', encoding='utf-8') as f:
#     md_text = f.read()

# # Convert Markdown to HTML
# html_text = markdown.markdown(md_text)

# # Path to wkhtmltopdf.exe
# path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# # Set config for pdfkit
# config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# # Convert HTML to PDF
# pdfkit.from_string(html_text, 'output.pdf', configuration=config)