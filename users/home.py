# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals

from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/', methods=['GET'])
def home_page():
    return render_template('home/home.html')
