#!/usr/bin/python3
"""Sign-up & log-in forms."""
from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, InputRequired
class EmailForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[Optional()])
    message = TextAreaField('Message', validators=[InputRequired(), Length(min=20, max=200)])
    submit = SubmitField('Submit')
    # price = IntegerField('Price', validators=[InputRequired()])
    # level = RadioField('Level',
    #                    choices=['Beginner', 'Intermediate', 'Advanced'],
    #                    validators=[InputRequired()])
    # available = BooleanField('Available', default='checked')
    # email = StringField('Title', validators=[InputRequired(),
    #                                         Length(min=10, max=100)])
