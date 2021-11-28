# User model
# Import the database object (db) from the main application module

from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from ..models import transaction, role


# user loader function
# Flask-login  will call it when it needs to retrieve information about the logged- in user.
@login_manager.user_loader
def load_user(user_id):
    '''try:
        return User.query.get(int(user_id))
    except:
        return None'''
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    nom = db.Column(db.String(64))
    prenom = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    creation_date = db.Column(db.DateTime)
    update_date = db.Column(db.DateTime)
    transactions = db.relationship(
        'Transaction', backref='user', lazy='dynamic')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.role is None:
            self.role = role.Role.query.filter_by(default=True).first()

    # To simplify the implementation of roles and permissions, a helper method can be added
    # to the User model that checks whether users have a given permission in the role they have been assigned
    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    # @property , if you want to have some conditions to set the value of an attribute in the class
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # the attribute name and the method name must be same which is used to set the value for the attribute
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '< User %r>' % self.username
