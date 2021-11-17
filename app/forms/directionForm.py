from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length
from wtforms import ValidationError
from ..models.direction import Direction



class DirectionForm(FlaskForm):
    name = StringField('Departement',validators=[DataRequired(),Length(1,64)])

    def validate_name(self,field):
        if Direction.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use')