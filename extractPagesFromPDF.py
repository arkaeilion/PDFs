import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("TrusteeMinuteResolution-01072019-30062020/TrusteeMinuteResolution-01072019-30062020.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    f = f'TMMR-page-{i}.pdf'
    with open(f, "wb") as outputStream:
        output.write(outputStream)