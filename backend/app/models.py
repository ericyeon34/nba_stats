from app import db # Import the database object from the app package which is an instance of SQLAlchemy
from sqlalchemy.ext.mutable import MutableList

# Defines the structure of the Players table in the database
class Players(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    retired = db.Column(db.Boolean)

    # nicknames = db.Column(MutableList.as_mutable(db.JSON))
    # alive = db.Column(db.Boolean)

    # birthdate = db.Column(db.Date)
    # height = db.Column(db.String(64), nullable=True)
    # weight = db.Column(db.Integer, nullable=True)
    # college = db.Column(db.String(64), nullable=True)
    # country = db.Column(db.String(64), nullable=True)
    # position = db.Column(MutableList.as_mutable(db.JSON))

    current_team = db.Column(db.String(64), nullable=True)
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

    def __repr__(self):
        return f'<Player {self.full_name} is mostly known as {self.nicknames[0]}>'

# class Teams(db.Model):
#     team_id = db.Column(db.Integer, primary_key=True)
#     team_name = db.Column(db.String(64), index=True)
#     team_abbreviation = db.Column(db.String(64))
#     team_location = db.Column(db.String(64))
#     team_conference = db.Column(db.String(64))
#     team_division = db.Column(db.String(64))
#     team_founded = db.Column(db.Integer)
#     team_colors = db.Column(db.ARRAY(db.String(64)))
#     team_mascot = db.Column(db.String(64))
#     team_championships = db.Column(db.Integer)
#     team_founder = db.Column(db.String(64))