# Stock model
# Import the database object (db) from the main application module

from app import db
from ..models import article



class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column( db.Integer, primary_key= True )
    quantite = db.Column(db.Integer, default =0)
    alerte = db.Column(db.Integer,default=0)
    creation_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    article_id = db.Column(db.Integer,db.ForeignKey('articles.id'))
    #name = db.Column(db.String(64),unique=True,nullable=False, index = True)

    def __repr__(self):
        return f'Stock(id={self.id}, quantite={self.quantite}, alerte={self.alerte})'

