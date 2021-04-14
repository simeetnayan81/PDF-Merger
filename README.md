# PDF-Merger
Python code to merge all the pdfs in a given directory.
This code merges all the pdf files in the current directory into a new pdf document. The files to be merged should be named in the order 1.pdf, 2.pdf, 3.pdf.....and so on. 
# Libraries Used:
1. pyPDF2 (Can be installed using the command "pip3 install pyPDF2" in the terminal)
2. os (Comes with python. No need to install explicitly)
# What it does:
The code counts the number of pdfs in the directory. The pdfs should be named in the order 1.pdf, 2.pdf, 3.pdf.....and so on. It iterates over all the files and reads them page by page and adds them sequentially in a new file named MergedFiles.pdf.
# Executing the Code:
Copy the code into the directory containing the pdfs. Open the terminal in the directory and run the code using "python mergePdfs.py".
