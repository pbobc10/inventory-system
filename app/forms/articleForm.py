from flask_wtf import FlaskForm
from sqlalchemy.orm import query
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired, InputRequired, Length, Regexp
from wtforms import ValidationError
from ..models.article import Article
from ..models.categorie import Categorie
from app.models import categorie


# Populate Select Categorie Field
class CategoryField(SelectField):
    """ Create a custom field to Populate the Categorie Select Field in th Form """
    def iter_choices(self):
        categories = [(el.id, el.name) for el in Categorie.query.all()]
        for value, label in categories:
            yield(value, label, self.coerce(value) == self.data)

    # def pre_validate(self, form):
    #     for v, _ in [(el.id, el.name) for el in Categorie.query.all()]:
    #         if self.data == v:
    #             break
    #         else:
    #             raise ValueError(self.gettext('Not a good choice'))


class RegistrationForm(FlaskForm):
    name = StringField('Article', validators=[DataRequired(), Length(1, 128), Regexp('^[A-Za-z][A-Za-z0-9_.]', flags=0, message='Usernames must have only letters,numbers, dots or \
                underscores')])
    categorie = CategoryField('Categorie', validators=[
                              InputRequired()])
    submit = SubmitField('Register')
    #categorie= SelectField('Categorie', choices=[(el.id,el.name)for el in  Categorie.query.all() ])

    #  When a form defines a method with the prefix validate_ followed by the name of a field, the method is invoked
    #  in addition to any regularly defined validators.

    def validate_name(self, field):
        if Article.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use')


class UpdateForm(FlaskForm):
    name = StringField('Article', validators=[DataRequired(), Length(1, 128), Regexp('^[A-Za-z][A-Za-z0-9_.]', flags=0, message='Usernames must have only letters,numbers, dots or \
                underscores')])
    categorie = CategoryField('Categorie', validators=[
                              InputRequired()])
    submit = SubmitField('Register')