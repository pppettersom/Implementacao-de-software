from flask import Flask
from .Hello.routes import hello_bp
from .models import db, User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
    app.register_blueprint(hello_bp)

    return app