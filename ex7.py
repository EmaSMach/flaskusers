# --*-- encoding: utf-8 --*--
from flask import Flask

app = Flask(__name__)


@app.route('/home/')
def home():
    return 'Welcome to the home page'

