# Article model
# Import the database object (db) from the main application module

from app import db
from ..models import stock,categorie,transaction



class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    stocks = db.relationship('Stock', backref='article', lazy='dynamic')
    creation_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    transactions = db.relationship(
        'Transaction', backref='article', lazy='dynamic')

    def __repr__(self):
        return f'Article(name = {self.name})'
