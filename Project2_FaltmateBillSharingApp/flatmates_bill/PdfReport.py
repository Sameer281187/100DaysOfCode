import os
import webbrowser

from fpdf import FPDF

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit= 'pt', format= 'A4')
        pdf.add_page()
        pdf.image(name="resource/house.png", w=50, h=50)

        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=40, txt="Flatmate's Bill", ln=1, align='C')
        pdf.cell(w=0, h=40, txt=f"Period: {bill.period}", ln=1, align='C')
        pdf.cell(w=0, h=40, txt="", ln=1, align='C')

        pdf.set_font(family="Times", style="B", size=18)
        pdf.cell(w=0, h=40, txt=f"{flatmate1.name}: INR {str(flatmate1.calculate_share_amount(bill, flatmate2))}", align='L', ln=1)
        pdf.cell(w=0, h=40, txt=f"{flatmate2.name}: INR {str(flatmate2.calculate_share_amount(bill, flatmate1))}", align='L')

        os.chdir("output")
        pdf.output(self.filename)
        webbrowser.open(self.filename)