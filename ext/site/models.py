# -*- encoding: utf-8 -*-
from ext.db import db

# Tabela de usuários
class Usuario(db.Model):
    __tablename__ = "usuario"
    id_usu = db.Column('id_usu', db.Integer, primary_key=True)
    usu = db.Column('usu', db.Unicode, unique = True)
    senha = db.Column('senha', db.Unicode)
    nome = db.Column('nome', db.Unicode, unique = True)
    email = db.Column('email', db.Unicode, unique = True)
    empresa = db.Column('empresa', db.Integer)
    empresa_empresa = db.Column('empresa_empresa', db.Integer, db.ForeignKey('empresa.empresa'))

    empresa = db.relationship('Empresa', foreign_keys=empresa_empresa)

# Controle de acesso
class ControlUsuario (db.Model):
    __tablename__ = "control_usuario "
    id = db.Column('id', db.Integer, primary_key=True)
    id_usu = db.Column('id_usu', db.Integer)
    admin = db.Column('admin', db.Boolean)
    modulo = db.Column('modulo', db.Integer)
    usuario_id_usu = db.Column('usuario_id_usu', db.Integer, db.ForeignKey('usuario.id_usu'))

    usuario = db.relationship('Usuario', foreign_keys=usuario_id_usu)

# Cadastro das empresas
class Empresa(db.Model):
    __tablename__ = "empresa"
    empresa = db.Column('empresa', db.Integer, primary_key=True)
    nome = db.Column('nome', db.Unicode)
    cnpj = db.Column('cnpj', db.Integer)
    endereco = db.Column('endereco', db.Unicode)
    telefone = db.Column('telefone', db.Unicode)
    cidade = db.Column('cidade', db.Unicode)
    uf = db.Column('uf', db.Unicode)
    email = db.Column('email', db.Unicode)
    responsavel = db.Column('responsavel', db.Unicode)

