def init_app(app):
    app.config["SECRET_KEY"] = "Carvalho577833"
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///vgcarvpro.db'

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
