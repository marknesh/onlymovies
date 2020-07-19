from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config

app=Flask(__name__,instance_relative_config=True)


bootstrap=Bootstrap(app)


app.config.from_object(Config)
app.config.from_pyfile('config.py')





from app import views

from app import error
