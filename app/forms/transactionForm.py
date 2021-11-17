from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from ..models.transaction import Transaction

HOUR_CHOICES = [('1', '8am'), ('2', '10am')]


class TransactionForm(FlaskForm):
    categorie = SelectField('Categorie', validators=[
        DataRequired()], choices=HOUR_CHOICES)
    article = SelectField('Article', validators=[
        DataRequired()], choices=HOUR_CHOICES)
    direction = SelectField('Departement', validators=[
        DataRequired()], choices=HOUR_CHOICES)

    quantity = IntegerField('Quatity', validators=DataRequired())
    receptionnaire = StringField('Receptionnaire', validators=[
                                 DataRequired(), Length(1, 64)])
    requisition = BooleanField('Requisition?', validators=DataRequired())

    def validate_quantity(self, field):
        pass
