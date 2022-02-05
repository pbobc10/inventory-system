# Departement model
# Import the database object (db) from the main application module

from app import db
from ..models import transaction



class Departement(db.Model):
    __tablename__ = 'departements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True, index=True, nullable=True)
    creation_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    transactions = db.relationship('Transaction',backref='departement',lazy='dynamic')

    def __repr__(self):
        return f'Departement(name={self.name})'