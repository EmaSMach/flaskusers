# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, NumberRange, Optional
from wtforms.widgets import TextArea

from utils.validators import IsInteger, PositiveInteger


class UserCreationForm(FlaskForm):
    """
    A simple form to submit user data.
    """
    user_id = IntegerField('User ID', validators=[
        DataRequired(message="Field required, only positive integers"),
        IsInteger(),
        NumberRange(min=1, message="User ID should be a positive number."),
    ])
    first_name = StringField('First Name', validators=[
        DataRequired("Field Required"),
        Length(min=3, max=50)
    ])
    last_name = StringField('Last Name', validators=[
        DataRequired(), Length(min=3, max=50)
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    active = BooleanField('Active')
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=30)])
    age = IntegerField('Age', validators=[Optional()])
    country = StringField('Country', validators=[Optional()])
    state = StringField('State', validators=[Optional()])
    city = StringField('City', validators=[Optional()])
    address = StringField('Address', widget=TextArea())
    zip_code = IntegerField('Zip Code', validators=[Optional(), PositiveInteger()])

    submit = SubmitField("Submit")
