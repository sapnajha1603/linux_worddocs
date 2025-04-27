from docx import Document

for i in range(2, 86):
    file = f"Tutorial_{i}.docx"
    doc = Document()
    doc.save(file)  # Properly saves as a .docx file
