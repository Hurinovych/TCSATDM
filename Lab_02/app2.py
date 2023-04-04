import docx

doc = docx.Document('Lab2_DockerBasics.docx')

for para in doc.paragraphs:
    print(para.text)