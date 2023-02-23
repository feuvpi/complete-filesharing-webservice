from flask import Flask
from flask_mysqldb import MySQL

db = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    from app.routes import main, upload, login, register, home

    app.register_blueprint(main.bp)
    app.register_blueprint(upload.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(register.bp)
    app.register_blueprint(home.bp)

    return app




