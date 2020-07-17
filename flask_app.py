# A very simple Flask Hello World app for you to get started with...

from flask import Flask

from vgcarvpro.ext import site
from vgcarvpro.ext import config
from vgcarvpro.ext import toolbar


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
