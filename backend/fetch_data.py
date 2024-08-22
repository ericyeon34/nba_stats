import pandas as pd
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats
from flaskr import app, db
from flaskr.models import Players

# ONLY RUN ONCE TO INPUT INTO DATABASE
# AFTER, USE UPDATE_PLAYERS_DATA.PY TO UPDATE THE DATABASE WITH NEW DATA

from sqlalchemy.exc import IntegrityError

def fetch_players_data():
    with app.app_context():
        # db.create_all()
        # Fetch all player IDs
        all_players = players._get_players()

        for player in all_players:
            career = playercareerstats.PlayerCareerStats(player_id=player['id']).get_dict()['resultSets']
            dict_career_totals_regular_season = next((item for item in career if item['name'] == 'CareerTotalsRegularSeason'), None)

            if dict_career_totals_regular_season:
                # Convert the data to a DataFrame
                df_career_totals_regular_season = pd.DataFrame(dict_career_totals_regular_season['rowSet'], columns=dict_career_totals_regular_season['headers'])
            
            if df_career_totals_regular_season.empty:
                continue

            existing_player = Players.query.filter_by(player_id=player['id']).first()

            print(player['full_name'])

            if existing_player:
                # Update existing player
                continue
                # existing_player.full_name = player['full_name']
                # existing_player.first_name = player['first_name']
                # existing_player.last_name = player['last_name']
                # existing_player.retired = player['is_active']
                # existing_player.current_team = teams.find_team_name_by_id(df_career_totals_regular_season['Team_ID'][0])
                # existing_player.games_played = df_career_totals_regular_season['GP'][0]
                # existing_player.games_started = df_career_totals_regular_season['GS'][0]
                # existing_player.minutes_played = df_career_totals_regular_season['MIN'][0]
                # existing_player.field_goals_made = df_career_totals_regular_season['FGM'][0]
                # existing_player.field_goals_attempted = df_career_totals_regular_season['FGA'][0]
                # existing_player.field_goal_percentage = df_career_totals_regular_season['FG_PCT'][0]
                # existing_player.three_pointers_made = df_career_totals_regular_season['FG3M'][0]
                # existing_player.three_pointers_attempted = df_career_totals_regular_season['FG3A'][0]
                # existing_player.three_point_percentage = df_career_totals_regular_season['FG3_PCT'][0]
                # existing_player.free_throws_made = df_career_totals_regular_season['FTM'][0]
                # existing_player.free_throws_attempted = df_career_totals_regular_season['FTA'][0]
                # existing_player.free_throw_percentage = df_career_totals_regular_season['FT_PCT'][0]
                # existing_player.offensive_rebounds = df_career_totals_regular_season['OREB'][0]
                # existing_player.defensive_rebounds = df_career_totals_regular_season['DREB'][0]
                # existing_player.total_rebounds = df_career_totals_regular_season['REB'][0]
                # existing_player.assists = df_career_totals_regular_season['AST'][0]
                # existing_player.steals = df_career_totals_regular_season['STL'][0]
                # existing_player.blocks = df_career_totals_regular_season['BLK'][0]
                # existing_player.turnovers = df_career_totals_regular_season['TOV'][0]
                # existing_player.personal_fouls = df_career_totals_regular_season['PF'][0]
                # existing_player.points = df_career_totals_regular_season['PTS'][0]
            else:
                # Add new player
                new_player = Players(
                    player_id=player['id'],
                    full_name=player['full_name'],
                    first_name=player['first_name'],
                    last_name=player['last_name'],
                    retired=player['is_active'],
                    current_team=teams.find_team_name_by_id(df_career_totals_regular_season['Team_ID'][0]),
                    games_played=df_career_totals_regular_season['GP'][0],
                    games_started=df_career_totals_regular_season['GS'][0],
                    minutes_played=df_career_totals_regular_season['MIN'][0],
                    field_goals_made=df_career_totals_regular_season['FGM'][0],
                    field_goals_attempted=df_career_totals_regular_season['FGA'][0],
                    field_goal_percentage=df_career_totals_regular_season['FG_PCT'][0],
                    three_pointers_made=df_career_totals_regular_season['FG3M'][0],
                    three_pointers_attempted=df_career_totals_regular_season['FG3A'][0],
                    three_point_percentage=df_career_totals_regular_season['FG3_PCT'][0],
                    free_throws_made=df_career_totals_regular_season['FTM'][0],
                    free_throws_attempted=df_career_totals_regular_season['FTA'][0],
                    free_throw_percentage=df_career_totals_regular_season['FT_PCT'][0],
                    offensive_rebounds=df_career_totals_regular_season['OREB'][0],
                    defensive_rebounds=df_career_totals_regular_season['DREB'][0],
                    total_rebounds=df_career_totals_regular_season['REB'][0],
                    assists=df_career_totals_regular_season['AST'][0],
                    steals=df_career_totals_regular_season['STL'][0],
                    blocks=df_career_totals_regular_season['BLK'][0],
                    turnovers=df_career_totals_regular_season['TOV'][0],
                    personal_fouls=df_career_totals_regular_season['PF'][0],
                    points=df_career_totals_regular_season['PTS'][0]
                )
                db.session.add(new_player)

            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                print(f"Failed to add/update player {player['full_name']} with ID {player['id']} due to integrity error.")

if __name__ == '__main__':
    fetch_players_data()