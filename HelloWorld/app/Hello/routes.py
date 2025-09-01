from flask import Blueprint

hello_bp  = Blueprint('hello',__name__)

@hello_bp.route('/')
def index():
    return "Hello Word"
@hello_bp.route('/sobre')
def about():
    return "Olá, Pettersom!"