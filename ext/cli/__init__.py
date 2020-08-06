import click
from ext.db import db
from ext.site import models #noqa

def init_app(app):
    @app.cli.command()
    def create_db():
        """este comando inicializa banco de dados"""
        db.create_all()

    @app.cli.command()
    def listar_usuarios():
        """Listar usuarios do sistema"""
        click.echo('lista de usuarios')