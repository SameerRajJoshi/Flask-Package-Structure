from os import environ
from flask import Flask
from config import Config

app=Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

from app import routes
