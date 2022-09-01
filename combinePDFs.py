import sys
import PyPDF2

dir = "Tax return-01072019-30062020/"

merger = PyPDF2.PdfFileMerger()
for f in ['TAXRETN-page-0.pdf', 'TAXRETN-page-1.pdf', 'TAXRETN-page-2.pdf', 'TAXRETN-page-3.pdf', 'TAXRETN-page-4.pdf',
            'TAXRETN-page-5.pdf', 'TAXRETN-page-6.pdf', 'TAXRETN-page-7.pdf', 'TAXRETN-page-8.pdf', 'TAXRETN-page-9.pdf', 
            'TAXRETN-page-10.pdf', 'TAXRETN-page-11.pdf', 'TAXRETN-page-12.pdf']:
    merger.append(PyPDF2.PdfFileReader(dir + f), 'rb')
with open('Tax return-01072019-30062020.pdf', 'wb') as new_file:
    merger.write(new_file)
