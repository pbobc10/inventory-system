from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from ..models.categorie import Categorie
from decimal import Decimal


# Populate Select Categorie Field
class Category(SelectField):
    def iter_choices(self):
        categories =[('','Select a Categorie')]+ [(el.id, el.name) for el in Categorie.query.all()]
        for value, label in categories:
            yield(value, label, self.coerce(value) == self.data)

    # def pre_validate(self, form):
    #     for v, _ in [(el.id, el.name) for el in Categorie.query.all()]:
    #         if self.data == v:
    #             break
    #         else:
    #             raise ValueError(self.gettext('Not a good Categorie'))


class RegistrationForm(FlaskForm):
    categorie = Category('Categorie', validators=[
        InputRequired()])
    article = SelectField('Article', validators=[InputRequired()],coerce=int,validate_choice=False,)
    quantite = IntegerField('Quantity', validators=[InputRequired(), NumberRange(
        min=Decimal('0'), message='The minimun value is 0')])
    alerte = IntegerField('Alerte', validators=[InputRequired(), NumberRange(
        min=Decimal('0'), message='The minimun value is 0')])
    submit = SubmitField('Register')


class UpdateForm(FlaskForm):
    categorie = Category('Categorie', validators=[
        InputRequired()])
    article = SelectField('Article', validators=[InputRequired()],coerce=int,validate_choice=False,)
    quantite = IntegerField('Quantity', validators=[InputRequired(), NumberRange(
        min=Decimal('0'), message='The minimun value is 0')])
    alerte = IntegerField('Alerte', validators=[InputRequired(), NumberRange(
        min=Decimal('0'), message='The minimun value is 0')])
    submit = SubmitField('Register')
