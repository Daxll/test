import PyPDF2

# PDF rotated first page

# with open('pdfs/210 dummy.pdf' , 'rb') as file :
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('pdfs/tilt_dummy.pdf' , 'wb') as file2 :
#         writer.write(file2)
#
# print('done!')

# pdf merger

# def pdf_merger (pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for i in pdf_list:
#         merger.append(i)
#     merger.write("pdfs/merged.pdf")
#
#
# input_list = ['pdfs/210 dummy.pdf', 'pdfs/210 twopage.pdf']
# pdf_merger(input_list)
# print('done!')

# pdf watermarker

def watermarker(file_name,watermark):
    template = PyPDF2.PdfFileReader(open('pdfs/'+file_name, 'rb'))
    watermark = PyPDF2.PdfFileReader(open('pdfs/'+watermark, 'rb'))
    output = PyPDF2.PdfFileWriter()
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open('pdfs/water_marked.pdf', 'wb') as file:
        output.write(file)
    return True

file = 'merged.pdf'
wm = '210 wtr.pdf'
watermarker(file,wm)
print('done!')
