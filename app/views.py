# Where we will create all our view functions.
from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Popular News'
    return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns the news source page and its article
    '''
    return render_template('news.html', id = news_id)