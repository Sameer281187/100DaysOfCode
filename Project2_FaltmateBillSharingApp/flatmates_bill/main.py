from Project2_FaltmateBillSharingApp.flatmates_bill.Bill import Bill
from Project2_FaltmateBillSharingApp.flatmates_bill.Flatmate import Flatmate
from Project2_FaltmateBillSharingApp.flatmates_bill.PdfReport import PdfReport

amount = float(input("Enter the monthly rent amount (in INR): "))
period = input("Enter the month and year for which this amount is for (eg. November 2025): ")
flatmate1_name = input("Enter the name of first flatmate: ")
flatmate1_days = int(input(f"Enter the no. of days {flatmate1_name} resided in the house during {period} :"))
flatmate2_name = input("Enter the name of second flatmate: ")
flatmate2_days = int(input(f"Enter the no. of days {flatmate2_name} resided in the house during {period} :"))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(flatmate1_days, flatmate1_name)
flatmate2 = Flatmate(flatmate2_days, flatmate2_name)

pdf_report = PdfReport(f"BillSharing_{the_bill.period}.pdf")
pdf_report.generate_pdf(flatmate1, flatmate2, the_bill)