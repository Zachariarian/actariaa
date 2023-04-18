from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_wtf import FlaskForm

from wtforms import StringField, DecimalField, DateField

from wtforms.validators import DataRequired, NumberRange

import os

# Create the Flask application instance

app = Flask(__name__)

# Set configuration options

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///loans.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database

db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Define the loan model

class Loan(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=False)

    interest_rate = db.Column(db.Float, nullable=False)

    date_submitted = db.Column(db.Date, nullable=False)

    def __repr__(self):

        return f'Loan(amount={self.amount}, interest_rate={self.interest_rate}, date_submitted={self.date_submitted})'

# Define the loan form

class LoanForm(FlaskForm):

    amount = DecimalField('Loan Amount', validators=[DataRequired(), NumberRange(min=0.01)])

    interest_rate = DecimalField('Interest Rate', validators=[DataRequired(), NumberRange(min=0.01, max=100)])

    date_submitted = DateField('Date Submitted', validators=[DataRequired()])

# Define the views

@app.route('/', methods=['GET', 'POST'])

def new_loan():

    form = LoanForm()

    if form.validate_on_submit():

        loan = Loan(amount=form.amount.data, interest_rate=form.interest_rate.data, date_submitted=form.date_submitted.data)

        db.session.add(loan)

        db.session.commit()

        return render_template('loan_submitted.html')

    return render_template('new_loan.html', form=form)

@app.route('/past_loans')

def past_loans():

    loans = Loan.query.all()

    return render_template('past_loans.html', loans=loans)

if __name__ == '__main__':

    app.run(debug=True)

