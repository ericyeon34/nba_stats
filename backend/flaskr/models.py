from flaskr import db # Import the database object from the app package which is an instance of SQLAlchemy
# from sqlalchemy.ext.mutable import MutableList

# Defines the structure of the Players table in the database
class Players(db.Model):
    """
    Model for the Players table.
    """
    player_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    retired = db.Column(db.Boolean)
    current_team = db.Column(db.String(64), nullable=True)

    # nicknames = db.Column(MutableList.as_mutable(db.JSON))
    # alive = db.Column(db.Boolean)

    # birthdate = db.Column(db.Date)
    # height = db.Column(db.String(64), nullable=True)
    # weight = db.Column(db.Integer, nullable=True)
    # college = db.Column(db.String(64), nullable=True)
    # country = db.Column(db.String(64), nullable=True)
    # position = db.Column(MutableList.as_mutable(db.JSON))

    # teams = db.Column(MutableList.as_mutable(db.JSON))
    # draft_year = db.Column(db.Integer, nullable=True)
    # draft_round = db.Column(db.Integer, nullable=True)
    # draft_number = db.Column(db.Integer, nullable=True)

    games_played = db.Column(db.Integer)
    games_started = db.Column(db.Integer)
    minutes_played = db.Column(db.Integer)
    field_goals_made = db.Column(db.Integer)
    field_goals_attempted = db.Column(db.Integer)
    field_goal_percentage = db.Column(db.Float)
    three_pointers_made = db.Column(db.Integer)
    three_pointers_attempted = db.Column(db.Integer)
    three_point_percentage = db.Column(db.Float)
    free_throws_made = db.Column(db.Integer)
    free_throws_attempted = db.Column(db.Integer)
    free_throw_percentage = db.Column(db.Float)
    # two_pointers_made = db.Column(db.Integer)
    # two_pointers_attempted = db.Column(db.Integer)
    # two_point_percentage = db.Column(db.Float)
    # effective_field_goal_percentage = db.Column(db.Float)
    offensive_rebounds = db.Column(db.Integer)
    defensive_rebounds = db.Column(db.Integer)
    total_rebounds = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    steals = db.Column(db.Integer)
    blocks = db.Column(db.Integer)
    turnovers = db.Column(db.Integer)
    personal_fouls = db.Column(db.Integer)
    points = db.Column(db.Integer)

    def to_dict(self):
        """
        Convert the object to a dictionary.
        """
        return {
            'player_id': self.player_id,
            'full_name': self.full_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'retired': self.retired,
            'current_team': self.current_team,

            'games_played': self.games_played,
            'games_started': self.games_started,
            'minutes_played': self.minutes_played,
            'field_goals_made': self.field_goals_made,
            'field_goals_attempted': self.field_goals_attempted,
            'field_goal_percentage': self.field_goal_percentage,
            'three_pointers_made': self.three_pointers_made,
            'three_pointers_attempted': self.three_pointers_attempted,
            'three_point_percentage': self.three_point_percentage,
            'free_throws_made': self.free_throws_made,
            'free_throws_attempted': self.free_throws_attempted,
            'free_throw_percentage': self.free_throw_percentage,
            'offensive_rebounds': self.offensive_rebounds,
            'defensive_rebounds': self.defensive_rebounds,
            'total_rebounds': self.total_rebounds,
            'assists': self.assists,
            'steals': self.steals,
            'blocks': self.blocks,
            'turnovers': self.turnovers,
            'personal_fouls': self.personal_fouls,
            'points': self.points
        }

    def __repr__(self):
        return f'<Player {self.full_name} is mostly known as {self.nicknames[0]}>'

# class Teams(db.Model):
#     team_id = db.Column(db.Integer, primary_key=True)
#     team_name = db.Column(db.String(64), index=True)
#     team_abbreviation = db.Column(db.String(64))
#     # team_location = db.Column(db.String(64))
#     team_city = db.Column(db.String(64))
#     team_state = db.Column(db.String(64))
#     team_arena = db.Column(db.String(64))
#     team_coach = db.Column(db.String(64))
#     team_founded_year = db.Column(db.DateTime)
#     team_championships = db.Column(db.Integer)
#     team_wins = db.Column(db.Integer)
#     team_losses = db.Column(db.Integer)
#     team_playoff_appearances = db.Column(db.Integer)
#     team_conference = db.Column(db.String(64))
#     team_division = db.Column(db.String(64))
#     # team_mascot = db.Column(db.String(64))
#     def __repr__(self):
#         return f'<Team {self.team_name} from {self.team_city}, {self.team_state}>'

# class Games(db.Model):
#     game_id = db.Column(db.Integer, primary_key=True)
#     game_date = db.Column(db.DateTime)
#     game_season = db.Column(db.String(64))
#     # game_location = db.Column(db.String(64))
#     game_home_team_id = db.Column(db.String(64))
#     game_away_team_id = db.Column(db.String(64))
#     game_home_team_score = db.Column(db.Integer)
#     game_away_team_score = db.Column(db.Integer)
#     game_winner = db.Column(db.String(64))
#     game_loser = db.Column(db.String(64))
#     game_overtime = db.Column(db.Boolean)
#     game_attendance = db.Column(db.Integer)
#     game_duration = db.Column(db.Integer)
#     game_playoff = db.Column(db.Boolean)
#     game_home_team_record = db.Column(db.String(64))
#     game_away_team_record = db.Column(db.String(64))

#     def __repr__(self):
#         return f'<Game {self.game_id} between {self.game_home_team} and {self.game_away_team} on {self.game_date}>'