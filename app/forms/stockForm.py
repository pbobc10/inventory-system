from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from ..models.stock import Stock


HOUR_CHOICES = [('1', '8am'), ('2', '10am')]


class StockForm(FlaskForm):
    article = SelectField('Article', validators=[
                          DataRequired()], choices=HOUR_CHOICES)
    quantity = IntegerField('Quantity', validators=DataRequired())
    alerte = IntegerField('Alerte', validators=DataRequired())

    def validate_alerte(self, field):
        pass
