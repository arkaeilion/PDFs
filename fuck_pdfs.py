import sys
import PyPDF2







# with open('TFN_decl.pdf', 'rb') as pdf_file:
#     pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#     pdf_writer = PyPDF2.PdfFileWriter()

#     for page_num in range(pdf_reader.numPages):
#         pdf_page = pdf_reader.getPage(page_num)
#         pdf_page.rotateClockwise(90)  # rotateCounterClockwise()

#         pdf_writer.addPage(pdf_page)

#     with open('TFN_decl_fix.pdf', 'wb') as pdf_file_rotated:
#         pdf_writer.write(pdf_file_rotated)



# merger = PyPDF2.PdfFileMerger()
# for f in ['TandC_0.pdf', 'TandC_fix.pdf']:
#     merger.append(PyPDF2.PdfFileReader(f), 'rb')
# with open('TandC_merge.pdf', 'wb') as new_file:
#     merger.write(new_file)