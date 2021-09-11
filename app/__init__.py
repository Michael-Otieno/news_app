# Where we will initialize our application.
from app.config import DevConfig
from flask import Flask

#initializing application
app = Flask(__name__)

#setting up configurations
app.config.from_object(DevConfig)

from app import views