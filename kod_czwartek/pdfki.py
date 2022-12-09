from fpdf import FPDF

lista = ['Tomek', 'Maciek', 'Grazynka', "Monika"]

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', 'B', size=14)
pdf.set_text_color(19, 83, 173)
pdf.cell(0, 5, str(lista))
pdf.ln()
pdf.set_font('Times', '', size=12)
pdf.set_text_color(0)
pdf.multi_cell(0, 5, "hello world " * 10)
pdf.ln()
pdf.multi_cell(0, 5, "Kolejne hello world " * 20, align='L')
pdf.output("hello_world.pdf")
