from app.source_test import ArticleTest
from app.models.source import Article
from flask import render_template
from app import app
from .request import get_sources,get_articles

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''

    #Getting news category
    source_general = get_sources('general')
    source_business = get_sources('business')
    source_technology = get_sources('technology')
    source_sports = get_sources('sports')
    source_entertainment = get_sources('entertainment')
    source_health = get_sources('health')
    source_science = get_sources('science')

    title = 'Welcome To The Best Popular News Website Online'
    return render_template('index.html', title = title, general = source_general,
     business = source_business, technology = source_technology, sports = source_sports,
     entertainment = source_entertainment, health = source_health, science = source_science )



@app.route('/source/<int:id>')
def source(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    source = get_sources(id)
    title = f'{source.title}'
    return render_template('source.html',title = title,source= source)

@app.route('/article/<int:id>')
def article(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_articles(id)
    title = f'{id}'
    return render_template('source.html',title = title,article= article, art=article)








# @app.route('/source/<source_id>')
# def artcicles(source_id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
    
#     return render_template('index.html',id = source_id)


