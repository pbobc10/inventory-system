from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length
from wtforms import ValidationError
from ..models.departement import Departement



class RegistrationForm(FlaskForm):
    name = StringField('Departement',validators=[DataRequired(),Length(1,64)])
    submit=SubmitField('Register')

    def validate_name(self,field):
        if Departement.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use')

class UpdateForm(FlaskForm):
    name = StringField('Departement',validators=[DataRequired(),Length(1,64)])
    submit=SubmitField('Register')