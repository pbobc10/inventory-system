from flask import request, render_template, url_for, Blueprint, flash, redirect, abort
from flask_login import login_required, login_user, logout_user
from ..models.user import User
from ..models.role import Permission, Role
from ..forms.authForm import LoginForm, RegistrationForm, UpdateRegistrationForm
from app import db


auth_blueprint = Blueprint(
    'auth', __name__, template_folder='../templates/auth')


# @auth_blueprint.route('/', methods=['GET', 'POST'])
# def index():
#     return redirect(url_for('login'))

@auth_blueprint.route('/', methods=['GET', 'POST'])
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('auth.display_users')
                flash('You are log in.')
            return redirect(next)

        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))


@auth_blueprint.route('/users', methods=['GET', 'POST'])
@login_required
def display_users():
    form = RegistrationForm()
    all_users = User.query.all()
    return render_template('register.html', form=form, all_users=all_users)


@auth_blueprint.route('/add/user', methods=['GET', 'POST'])
@login_required
def add_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        # checked username for uniqueness after the form validation is complite
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already in use.')
            return redirect(url_for('auth.display_users'))

        user = User(username=form.username.data, nom=form.nom.data, prenom=form.prenom.data,
                    password=form.password.data, role=Role.query.filter_by(name=form.user_role.data).first())
        db.session.add(user)
        db.session.commit()
        flash('user Register.')
    if form.errors:
        flash(form.errors, 'danger')
    return redirect(url_for('auth.display_users'))


@auth_blueprint.route('/update/user/<int:id>', methods=['GET', 'POST'])
@login_required
def update_user(id):
    user = User.query.filter_by(id=id).first()
    form = UpdateRegistrationForm()

    if user is None:
        abort(404)

    if form.validate_on_submit():
        user.nom = form.nom.data
        user.prenom = form.prenom.data
        user.password = form.username.data  # reset password with the username
        user.role = Role.query.filter_by(name=form.user_role.data).first()
        db.session.commit()
        return redirect(url_for('auth.display_users'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('update_user.html', form=form, user=user)


@auth_blueprint.route('/delete/user/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('auth.display_users'))


# make Permission object available in the template
@auth_blueprint.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
