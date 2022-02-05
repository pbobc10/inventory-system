from flask import render_template, redirect, url_for, Blueprint, jsonify
import flask
from flask.helpers import flash
from flask_login import login_required
from flask_wtf import form

from app.models.categorie import Categorie
from ..models.stock import Stock
from ..models.article import Article
from ..forms.stockForm import RegistrationForm, UpdateForm
from app import db


stock_blueprint = Blueprint(
    'stock', __name__, template_folder='../templates/stock')


@stock_blueprint.route('/stock', methods=['GET', 'POST'])
@login_required
def display_stocks():
    form = RegistrationForm()
    stocks = db.session.query(Article.name,Stock.id, Stock.quantite, Stock.alerte,Stock.update_date, Stock.creation_date).filter(Stock.article_id == Article.id).all()
    return render_template('stock.html', form=form, stocks=stocks)


@stock_blueprint.route('/add/stocks', methods=['GET', 'POST'])
@login_required
def add_stock():
    form = RegistrationForm()
    print(form.article.data)
    if form.validate_on_submit():
        print('test stock!!!!')
        print("test Stock",form.quantite.data,form.alerte.data,form.article.data)
        stock = Stock(quantite=form.quantite.data, alerte=form.alerte.data,
                      article_id=form.article.data)
        try:
            db.session.add(stock)
            db.session.commit()
        except Exception as e:
            print('db',e)
        flash('Stock Registered', 'success')

    if form.errors:
        flash(form.errors, 'danger')
    return redirect(url_for('stock.display_stocks'))


@stock_blueprint.route('/update/stocks/<int:id>', methods=['GET', 'POST'])
@login_required
def update_stock(id):
    form = UpdateForm()
    stock_categorie_id = db.session.query(Article.categorie_id).filter(Stock.article_id == Article.id).filter(Stock.id==id).first()[0] 
    stock=Stock.query.get_or_404(id)
    if form.validate_on_submit():
        stock.article_id = Article.query.filter_by(
            name=form.article.data).first()
        stock.quantite = form.quantite.data
        stock.alert = form.alerte.data
        db.session.add(stock)
        db.session.commit()
        flash('Stock Updated', 'success')
        return redirect(url_for('stock.display_stocks'))

    if form.errors:
        flash(form.errors, 'danger')

    return render_template('update_stock.html', form=form, stock=stock,stock_categorie_id=stock_categorie_id)


@stock_blueprint.route('/delete/stocks/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_stock(id):
    stock = Stock.query.get_or_404(id)
    db.session.delete(stock)
    db.session.commit()
    flash('Stock Deleted', 'success')
    return redirect(url_for('stock.display_stocks'))


@stock_blueprint.route('/articles/<int:categorie_id>')
@login_required
def article_to_Json(categorie_id):
    articles = Article.query.filter_by(
        categorie=Categorie.query.get_or_404(categorie_id)).all()
    articleArray = []
    for article in articles:
        articleObject = {}
        articleObject['id'] = article.id
        articleObject['name'] = article.name
        articleArray.append(articleObject)
    return jsonify({'articles': articleArray})
