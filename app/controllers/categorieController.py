from os import name
from flask import Flask,request,redirect,abort,url_for,Blueprint
from flask.helpers import flash
from flask.templating import render_template
from flask_login import login_required
from ..models.categorie import Categorie
from ..forms.categorieForm import RegistrationForm,UpdateRegistrationForm
from app import db


categorie_blueprint = Blueprint('categorie','__name__',template_folder='../templates/categorie')

@categorie_blueprint.route('/categories',methods=['GET','POST'])
@login_required
def display_categories():
    form=RegistrationForm()
    all_categories =  Categorie.query.all()
    if all_categories is None:
        abort(404)
    else:
        return render_template('categorie/categorie.html',all_categories=all_categories,form=form)

@categorie_blueprint.route('/add/categories',methods=['GET','POST'])
@login_required
def add_categorie():
    form=RegistrationForm()
    if form.validate_on_submit():
        categorie = Categorie(name=form.name.data)
        db.session.add(categorie)
        db.session.commit()
        flash('Categorie register','message')

    if form.errors:
        flash(form.errors,'danger')
    return redirect(url_for('categorie.display_categories'))

@categorie_blueprint.route('/update/categorie/<int:id>',methods=['GET','POST'])
def update_categorie(id):
    form=UpdateRegistrationForm()
    categorie= Categorie.query.filter_by(name=form.name.data).get_or_404(id)
    if form.validate_on_submit():
            categorie.name = form.name.data
            db.session.add(categorie)
            db.session.commit()
            flash('Categorie updates','message')
            return redirect(url_for('categorie.display_categories'))
    
    if form.errors:
        flash(form.errors,'error')

    render_template('categorie/update_categorie.html',form=form,categorie=categorie)