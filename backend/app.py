from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Define a route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask Backend!"})

# Define another route (e.g., for player stats)
@app.route('/player/<string:player_id>', methods=['GET'])
def get_player_stats(player_id):
    # Dummy data example
    player_stats = {
        "player_id": player_id,
        "name": "LeBron James",
        "team": "Los Angeles Lakers",
        "games_played": 72,
        "average_pts": 27.3
    }
    return jsonify(player_stats)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
