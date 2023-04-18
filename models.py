from datetime import datetime

from app import db

class Loan(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    loan_type = db.Column(db.String(20), nullable=False)

    loan_amount = db.Column(db.Float)

    interest_rate = db.Column(db.Float, nullable=False)

    loan_duration = db.Column(db.Integer, nullable=False)

    monthly_payment = db.Column(db.Float, nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        return f"Loan('{self.loan_type}', '{self.loan_amount}', '{self.interest_rate}', '{self.loan_duration}', '{self.monthly_payment}', '{self.date_created}')"

