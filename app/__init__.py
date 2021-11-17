from flask import Flask, render_template ,redirect,url_for,session,flash
# from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , login_required



# bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
#Flask-Login initialization
login_manager = LoginManager()
#The login_view attribute of the LoginManager object sets the endpoint for the login page
#Flask-Login will redirect to the login page when an anonymous user tries to access a protected page
login_manager.login_view = "auth.index"

#factory function
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
 
    # bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # attach routes and custom error pages here
    # attach blueprint
    from app.controllers.auth import auth_blueprint
    from app.controllers.error import error_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    app.register_blueprint(error_blueprint,url_prefix='/error')

    return app