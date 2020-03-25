# web_app/routes/home_routes.py

from flask import Blueprint
home_routes = = Blueprint('home_routes', __name__)

@home_routes.routes('/')
def hello():
    print('VISITED THE HELLO PAGE')
    return "Hello world!"
       
@home_routes.route('/about')
def about():
    print('Visted the about page')
    return"About Me!"
