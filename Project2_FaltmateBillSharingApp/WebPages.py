from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from wtforms.validators import DataRequired

from flatmates_bill.Flatmate import Flatmate
from flatmates_bill.Bill import Bill

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template("index.html")



class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html", billForm=bill_form)



class ResultsPage(MethodView):
    def post(self):
        billForm = BillForm(request.form)

        the_bill = Bill(amount=float(billForm.amount.data), period=billForm.period.data)
        flatmate1 = Flatmate(days_in_house=float(billForm.days_in_house_flatmate1.data), name=billForm.name_flatmate1.data)
        flatmate2 = Flatmate(days_in_house=float(billForm.days_in_house_flatmate2.data), name=billForm.name_flatmate2.data)

        return render_template("results.html", name1= flatmate1.name,
                               amount1= flatmate1.calculate_share_amount(the_bill, flatmate2),
                               name2= flatmate2.name,
                               amount2= flatmate2.calculate_share_amount(the_bill, flatmate1))



class BillForm(Form):
    amount = StringField('Bill Amount: ', validators=[DataRequired()])
    period = StringField('Bill Period: ', validators=[DataRequired()])

    name_flatmate1 = StringField('Name Flatmate1: ', validators=[DataRequired()])
    days_in_house_flatmate1 = StringField('Days in House Flatmate1: ', validators=[DataRequired()])

    name_flatmate2 = StringField('Name Flatmate2: ', validators=[DataRequired()])
    days_in_house_flatmate2 = StringField('Days in House Flatmate2: ', validators=[DataRequired()])

    calculate_button = SubmitField('Calculate')



app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))

app.run()