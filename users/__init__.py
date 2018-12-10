# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals
import os
from flask import Flask, render_template

import users
import home


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        #WTF_CSRF_ENABLED=True,
        SECRET_KEY='dev',  # 220e7fafb945fdf9bc5fd6fca216bdb2c92aeff019cc8f8e73c0271d9afef3a40c7becd23883cc837b77d304f1775dc51908
        DATABASE=os.path.join(app.instance_path, 'users.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Start registering our blueprints
    app.register_blueprint(users.bp)
    app.register_blueprint(home.bp)

    return app

