# A very simple Flask Hello World app for you to get started with...

from flask import Flask

from ext import site
from ext import config
from ext import toolbar
from ext import db
from ext import cli

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    #toolbar.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    site.init_app(app)
    return app
# flask no pythonanyware
my_app = create_app()