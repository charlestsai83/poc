from flask import Flask

def creat_app():
    app = Flask('__main__')
    from .main import main
    app.register_blueprint(main)
    return app
