from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    data = {'message': 'Welcome to the API!'}
    return jsonify(data)
