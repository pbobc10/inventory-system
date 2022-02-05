from flask import render_template,redirect,url_for,flash,Blueprint
from flask_login.utils import login_required
from ..models.article import Article
from ..models.categorie import Categorie
from ..forms.articleForm import RegistrationForm,UpdateForm
from app import db



# create the blueprint
article_blueprint=Blueprint('article',__name__,template_folder='../templates/article')

@article_blueprint.route('/articles/',methods=['GET','POST'])
@login_required
def display_articles():
    form = RegistrationForm()
    articles = Article.query.all()
    return render_template('article.html',form=form,articles=articles)

@article_blueprint.route('/add/articles',methods=['GET','POST'])
@login_required
def add_article():
    form = RegistrationForm()
    print('test categorie',form.categorie.data)

    if form.validate_on_submit():
        article = Article(name=form.name.data,categorie=Categorie.query.filter_by(id=form.categorie.data).first())
        db.session.add(article)
        db.session.commit()
        flash('Article Register','success')
        #return redirect(url_for('article.display_articles'))

    if form.errors:
        flash(form.errors,'danger')
    return redirect(url_for('article.display_articles'))

@article_blueprint.route('/update/article/<int:id>',methods=['GET','POST'])
@login_required
def update_article(id):
    form=UpdateForm()
    article = Article.query.get_or_404(id)
    if form.validate_on_submit():
        article.categorie=Categorie.query.filter_by(id=form.categorie.data).first()
        article.name =form.name.data
        db.session.commit()
        flash('Article Update','success')
        return redirect(url_for('article.display_articles'))

    if form.errors:
        flash(form.errors,'danger')
    return render_template('update_article.html',form=form,article=article)


@article_blueprint.route('/delete/article/<int:id>',methods=['GET','POST'])
@login_required
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Article deleted','success')
    return redirect(url_for('article.display_articles'))