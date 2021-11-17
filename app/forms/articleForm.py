from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from ..models.article import Article


class ArticleForm(FlaskForm):
    categorie_id = StringField('Categorie', validators=DataRequired())
    name = StringField('Article', validators=[DataRequired(), Length(1, 64)])

    #  When a form defines a method with the prefix validate_ followed by the name of a field, the method is invoked
    #  in addition to any regularly defined validators.

    def validate_name(self, field):
        if Article.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use')
