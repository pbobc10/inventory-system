from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
from wtforms import ValidationError
from ..models.user import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]', flags=0, message='Usernames must have only letters,numbers, dots or \
                underscores')])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(1, 64)])
    remember_me = BooleanField('Keep me Logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]', flags=0, message='Usernames must have only letters, numbers, dots or \
               underscores')])
    nom = StringField('Last name', validators=[DataRequired(), Length(1, 64)])
    prenom = StringField('First name', validators=[
                         DataRequired(), Length(1, 64)])
    user_role = SelectField('Role',  choices=[
                            'Admin', 'Advence', 'Moderate', 'User'])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'password_2', message='Passwords must match.')])
    password_2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    #  When a form defines a method with the prefix validate_ followed by the name of a field, the method is invoked
    #  in addition to any regularly defined validators.
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            flash('Username already in use.')
            raise ValidationError('Username already in use.')


class UpdateRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]', flags=0, message='Usernames must have only letters, numbers, dots or \
               underscores')])
    nom = StringField('Last name', validators=[DataRequired(), Length(1, 64)])
    prenom = StringField('First name', validators=[
                         DataRequired(), Length(1, 64)])
    user_role = SelectField('Role',  choices=[
                            'Admin', 'Advence', 'Moderate', 'User'])
    submit = SubmitField('Register')