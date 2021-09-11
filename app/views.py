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