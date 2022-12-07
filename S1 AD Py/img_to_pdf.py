from fpdf import FPDF
pdf = FPDF()

lst = ['test_qr.png']

for image in lst:
    pdf.add_page()
    pdf.image(image)
    pdf.output('test_pdf.pdf', 'F')