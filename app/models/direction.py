# Direction model
# Import the database object (db) from the main application module

from app import db
from ..models import transaction



class Direction(db.Model):
    __tablename__ = 'directions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True, index=True, nullable=True)
    transactions = db.relationship('Transaction',backref='direction',lazy = 'dynamic')

    def __repr__(self):
        return f'Direction(name={self.name})'