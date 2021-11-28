from flask.helpers import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from ..models.categorie import Categorie


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)])
    submit=SubmitField('Register')

    #  When a form defines a method with the prefix validate_ followed by the name of a field, the method is invoked
    #  in addition to any regularly defined validators.

    def validate_name(self, field):
        if Categorie.query.filter_by(name=field.data).first():
            flash('Name already in use')
            raise ValidationError('Name already in use')


class UpdateRegistrationForm(FlaskForm):
    name = StringField('Name',[DataRequired(),Length(1,64)])
    submit=SubmitField('Register')

    