#install Pypdf package - pip3 install PYPDF2
import PyPDF2
import sys
import os
print("Merge PDFs here! ")
merger = PyPDF2.PdfMerger()
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combinedresume.pdf")    
      
