from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, URL, Optional
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Confirm Password and Password do not match')])
    submit = SubmitField('Sign Up')

    # checking if username exist in db
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist in database')
        

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SnippetForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    code_content = TextAreaField('Code Content', validators=[DataRequired()])
    language = StringField('Language', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired()])
    notes = TextAreaField('Notes', validators=[Optional()])
    source_url = StringField('Source URL', validators=[Optional(), URL(message='Enter valid URL'), Length(max=255)])
    tags = StringField('Tags (comma-seperated)', validators=[Optional(), Length(max=255)])
    submit = SubmitField('Save Snippet')