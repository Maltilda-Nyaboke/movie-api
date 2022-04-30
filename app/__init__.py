from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
import os

# Initializing application
app = Flask(__name__,instance_relative_config= True)

SECRET_KEY = os.urandom(32)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

from app import error
bootstrap = Bootstrap(app)
