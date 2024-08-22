from flask import jsonify, Blueprint
from flaskr.models import Players

# Create a blueprint for the main routes
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    Route to display a welcome message.
    """
    return "Welcome to the NBA Game API!"

@bp.route('/players')
def players():
    """
    Route to get all players.
    """
    all_players = Players.query.all()
    return jsonify([player.to_dict() for player in all_players])

@bp.route('/player/<int:player_id>')
def player(player_id):
    """
    Route to get a specific player by ID.
    """
    player = Players.query.get_or_404(player_id)
    return jsonify(player.to_dict())