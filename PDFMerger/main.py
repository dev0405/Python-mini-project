from PyPDF2 import PdfWriter
merger=PdfWriter()

pdfs=[]
n=int(input("Enter the number of pdf you want to join : "))
for i in range(0,n):
    name=input(f"Enter the name of the pdf {i+1} : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
