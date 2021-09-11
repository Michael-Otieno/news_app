# Where we will create all our view functions.
from app.models import source
from flask import render_template
from app import app
from request import get_sources

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

@app.route('/source/<source_id>')
def news(source_id):
    '''
    View news page function that returns the news source page and its article
    '''
    return render_template('source.html', id = source_id)