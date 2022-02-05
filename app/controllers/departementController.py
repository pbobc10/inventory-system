from os import name
from flask import Flask,request,redirect,abort,url_for,Blueprint
from flask.helpers import flash
from flask.templating import render_template
from flask_login import login_required
from ..models.departement import Departement
from ..forms.departementForm import RegistrationForm,UpdateForm
from app import db


departement_blueprint = Blueprint('departement',__name__,template_folder='../templates/departement')

@departement_blueprint.route('/departements',methods=['GET','POST'])
@login_required
def display_departements():
    form=RegistrationForm()
    all_departements =  Departement.query.all()
    if all_departements is None:
        abort(404)
    else:
        return render_template('departement/departement.html',all_departements=all_departements,form=form)

@departement_blueprint.route('/add/departements',methods=['GET','POST'])
@login_required
def add_departement():
    form=RegistrationForm()
    if form.validate_on_submit():
        departement = Departement(name=form.name.data)
        db.session.add(departement)
        db.session.commit()
        flash('Departement registered','success')

    if form.errors:
        flash(form.errors,'danger')
    return redirect(url_for('departement.display_departements'))

@departement_blueprint.route('/update/departement/<int:id>',methods=['GET','POST'])
@login_required
def update_departement(id):
    form=UpdateForm()
    departement= Departement.query.get_or_404(id)
    if form.validate_on_submit():
            departement.name = form.name.data
            db.session.add(departement)
            db.session.commit()
            flash('Departement updated','success')
            return redirect(url_for('departement.display_departements'))
    
    if form.errors:
        flash(form.errors,'danger')

    return render_template('departement/update_departement.html',form=form,departement=departement)

@departement_blueprint.route('/delete/departement/<int:id>',methods=['GET','POST'])
@login_required
def delete_departement(id):
    departement= Departement.query.get_or_404(id)
    db.session.delete(departement)
    db.session.commit()
    flash('Categorie deleted','success')
    return redirect(url_for('departement.display_departements'))