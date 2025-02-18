from flask import Blueprint, request, jsonify

# Create a Blueprint instance
user_bp = Blueprint('user_bp', __name__)

# Define routes
@user_bp.route('/players', methods=['GET'])
def get_players():
    return jsonify({"message": "List of players"})

@user_bp.route('/players', methods=['POST'])
def create_player():
    data = request.get_json()
    return jsonify({"message": "Player created", "data": data}), 201

@user_bp.route('/players/<string:player_id>', methods=['GET'])
def get_player(player_id):
    return jsonify({"message": f"Player with ID {player_id}"})

@user_bp.route('/players/<string:player_id>', methods=['PUT'])
def update_player(player_id):
    data = request.get_json()
    return jsonify({"message": f"Player {player_id} updated", "data": data})

@user_bp.route('/players/<string:player_id>', methods=['DELETE'])
def delete_player(player_id):
    return jsonify({"message": f"Player {player_id} deleted"})
