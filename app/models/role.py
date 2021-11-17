# Role model
# Import the database object (db) from the main application module

from app import db
from ..models import user


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    permissions = db.Column(db.Integer)
    default = db.Column(db.Boolean, default=False, index=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def __repr__(self):
        ''' print object in this format '''
        return '< Role : %r>' % self.name

    def has_permission(self, perm):
        ''' check if the permission is already assign '''
        return self.permissions & perm == perm

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions |= perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions ^= perm

    def resset_permission(self):
        self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.DASHBOARD, Permission.CHANGE_PASSWORD],
            'Moderate': [Permission.DASHBOARD, Permission.CHANGE_PASSWORD, Permission.TRANSACTIONS],
            'Advence': [Permission.DASHBOARD, Permission.CHANGE_PASSWORD, Permission.TRANSACTIONS, Permission.DEPARTEMENT,Permission.ARTICLE ,Permission.CATEGORIE],
            'Admin': [Permission.DASHBOARD, Permission.CHANGE_PASSWORD, Permission.TRANSACTIONS, Permission.DEPARTEMENT,Permission.ARTICLE , Permission.CATEGORIE, Permission.USER]
        }

        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.resset_permission()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()


class Permission:
    ''' permission constants '''
    DASHBOARD = 1
    CHANGE_PASSWORD = 2
    TRANSACTIONS = 4
    DEPARTEMENT = 8
    ARTICLE = 16
    CATEGORIE = 32
    USER = 64
