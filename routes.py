from flask import Blueprint, jsonify

example_bp = Blueprint('example', __name__)

@example_bp.route('/example_route')
def example_route():
    return jsonify({'message': 'This is an example route!'})
