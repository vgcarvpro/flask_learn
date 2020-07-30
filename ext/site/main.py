from flask import render_template
from flask import Blueprint
from flask import current_app

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    print("entrei na funcao main")
    current_app.logger.debug("Entrei na funcao main")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/testes")
def restaurants():
    return render_template("testes.html")


@bp.route("/gerador")
def gerador():
    return render_template("gerador.html")