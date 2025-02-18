from flask import Blueprint, request, jsonify

# Create a Blueprint instance
user_bp = Blueprint('user_bp', __name__)

# Define routes
@user_bp.route('/players', methods=['GET'])
def get_users():
    return jsonify({"message": "List of users"})

@user_bp.route('/players', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"message": "User created", "data": data}), 201

@user_bp.route('/players/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({"message": f"User with ID {user_id}"})

@user_bp.route('/players/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return jsonify({"message": f"User {user_id} updated", "data": data})

@user_bp.route('/players/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify({"message": f"User {user_id} deleted"})
