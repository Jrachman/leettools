from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField
from datetime import datetime
import 


class ChoiceForm(FlaskForm):
    diff_range = SelectField('Difficulty', choices=[
        ('e', 'Easy'),
        ('em', 'Easy / Medium'),
        ('m', 'Medium'),
        ('mh', 'Medium / Hard'),
        ('h', 'Hard')
    ])

    grind_per = IntegerField('Grind Duration (Days)')

    today = datetime.today()
    choices_month = [(i, i) for i in range(1, 13)]
    choices_day = [(i, i) for i in range(1, 32)]
    choices_year = [(i, i) for i in range(today.year, today.year + 11)]
    start_month = SelectField('Month', coerce=int, default=today.month, choices=choices_month)
    start_day = SelectField('Day', coerce=int, default=today.day, choices=choices_day)
    start_year = SelectField('Year', coerce=int, default=today.year, choices=choices_year)

    submit = SubmitField("Submit")


class ResultForm(FlaskForm):
