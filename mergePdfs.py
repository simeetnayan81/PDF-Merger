'''This code merges all the pdf files in the current directory into a new pdf document.
The files to be merged should be named in the order 0.pdf, 1.pdf, 2.pdf.....and so on''' 

#imports pyPDF2 Library
import os
import PyPDF2 
 
lst= os.listdir(os.getcwd())
pdflst=list(filter(lambda x: '.pdf' in x, lst))
l=len(pdflst)#number of pdfs in the current directory


# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()
#loop through all the files present in the directory
for i in range(l):
	#open the file to be merged one by one. The files must be saved in order 0.pdf, 1.pdf, 2.pdf.....so on 
	pdfInputFile = open(str(i+1)+'.pdf', 'rb')
	# Read the files that you have opened
	pdfReader = PyPDF2.PdfFileReader(pdfInputFile) 
# Loop through all the pagenumbers for the first document
	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)
 
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
 
# close all the created and opened files
pdfOutputFile.close()
pdfInputFile.close()



'''By Simeet Nayan'''