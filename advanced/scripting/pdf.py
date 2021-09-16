# It is necessary to install PyPDF2 'pip install PyPDF2'

# Example of input: python pdf.py ./files/pdfs/ dummy.pdf twopage.pdf tilt.pdf

import PyPDF2

import sys

path = sys.argv[1]
inputs = sys.argv[2:] # Grab all the arguments after the second one and keep them in a list

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:    
        print(pdf)
        merger.append(path + pdf)
    merger.write(path + 'super.pdf')

pdf_combiner(inputs)

# Working with PDFs:
"""
with open('./files/pdfs/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    print(page)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./files/pdfs/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

"""
