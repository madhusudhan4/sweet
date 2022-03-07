import PyPDF2

f=open("C:/Users/rajug/Downloads/datafile/data.pdf",'rb')
data=PyPDF2.PdfFileReader(f)
print(data)

