# Direction model
# Import the database object (db) from the main application module

from app import db
from ..models import article,departement,user



class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    quantite = db.Column(db.Integer, default=0)
    receptionnaire = db.Column(db.String(64), nullable=False)
    requisition = db.Column(db.Boolean, default=False)
    creation_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    departement_id = db.Column(db.Integer, db.ForeignKey('departements.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'Transaction(id={self.id}, quantite={self.quantite})'
