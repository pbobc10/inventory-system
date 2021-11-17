# Categorie model
# Import the database object (db) from the main application module

from app import db
from ..models import article



class Categorie(db.Model):
    __tablename__  = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    articles = db.relationship('Article',backref='categorie',lazy = 'dynamic')


    def __repr__(self):
        return f'Categorie(name = { self.name})'
