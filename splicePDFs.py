import sys
import PyPDF2

writer = PyPDF2.PdfFileWriter()

mainPDF = '2020 Representation Letter EJ Haggart Super 1.pdf'
page0 = '2.pdf'

readerMain = PyPDF2.PdfFileReader(mainPDF)
readerPage0 = PyPDF2.PdfFileReader(page0)



for i in range(readerMain.numPages):
    page = readerMain.getPage(i)

    if i == 5: page = readerPage0.getPage(0)

    page.compressContentStreams()
    writer.addPage(page)


with open('2020 Representation Letter EJ Haggart Super 1 signed.pdf', 'wb') as new_file:
    writer.write(new_file)