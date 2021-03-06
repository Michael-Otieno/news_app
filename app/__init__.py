# Where we will initialize our application.
from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap

#initializing application
app = Flask(__name__, instance_relative_config=True)

#setting up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing flask extensions
bootstrap = Bootstrap(app)


from app import views
from app import error