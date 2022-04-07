from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, \
                    PasswordField, BooleanField, SubmitField, SearchField, EmailField, MultipleFileField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Submit")
