import pandas as pd
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playerindex
from app import app, db
from app.models import Players

# ONLY RUN ONCE TO INPUT INTO DATABASE
# AFTER, USE UPDATE_PLAYERS_DATA.PY TO UPDATE THE DATABASE WITH NEW DATA

def fetch_players_data():
    with app.app_context():
        db.create_all()
        # Fetch all player IDs
        all_players = players._get_players()
        # all_players = {id, full_name, first_name, last_name, is_active}

        # Fetch player career stats
        career = playercareerstats.PlayerCareerStats(player_id=all_players[0]['id']).get_dict()['resultSets']
        dict_career_totals_regular_season = next((item for item in career if item['name'] == 'CareerTotalsRegularSeason'), None)

        if dict_career_totals_regular_season:
            # Convert the data to a DataFrame
            df_career_totals_regular_season = pd.DataFrame(dict_career_totals_regular_season['rowSet'], columns=dict_career_totals_regular_season['headers'])
        
        # print(f'''
        #     player_id = {all_players[0]['id']},
        #     full_name = {all_players[0]['full_name']},
        #     first_name = {all_players[0]['first_name']},
        #     last_name = {all_players[0]['last_name']},
        #     retired = {all_players[0]['is_active']},

        #     nicknames = ,
        #     alive = ,

        #     birthdate = ,
        #     height = ,
        #     weight = ,
        #     college = ,
        #     country = ,
        #     position = ,

        #     current_team = {teams.find_team_name_by_id(df_career_totals_regular_season['Team_ID'][0])},
        #     teams = ,
        #     draft_year = ,
        #     draft_round = ,
        #     draft_number = ,

        #     games_played = {df_career_totals_regular_season['GP'][0]},
        #     games_started = {df_career_totals_regular_season['GS'][0]},
        #     minutes_played = {df_career_totals_regular_season['MIN'][0]},
        #     field_goals_made = {df_career_totals_regular_season['FGM'][0]},
        #     field_goals_attempted = {df_career_totals_regular_season['FGA'][0]},
        #     field_goal_percentage = {df_career_totals_regular_season['FG_PCT'][0]},
        #     three_pointers_made = {df_career_totals_regular_season['FG3M'][0]},
        #     three_pointers_attempted = {df_career_totals_regular_season['FG3A'][0]},
        #     three_point_percentage = {df_career_totals_regular_season['FG3_PCT'][0]},
        #     free_throws_made = {df_career_totals_regular_season['FTM'][0]},
        #     free_throws_attempted = {df_career_totals_regular_season['FTA'][0]},
        #     free_throw_percentage = {df_career_totals_regular_season['FT_PCT'][0]},
        #     offensive_rebounds = {df_career_totals_regular_season['OREB'][0]},
        #     defensive_rebounds = {df_career_totals_regular_season['DREB'][0]},
        #     total_rebounds = {df_career_totals_regular_season['REB'][0]},
        #     assists = {df_career_totals_regular_season['AST'][0]},
        #     steals = {df_career_totals_regular_season['STL'][0]},
        #     blocks = {df_career_totals_regular_season['BLK'][0]},
        #     turnovers = {df_career_totals_regular_season['TOV'][0]},
        #     personal_fouls = {df_career_totals_regular_season['PF'][0]},
        #     points = {df_career_totals_regular_season['PTS'][0]}
        #       ''')

        player = Players(
            player_id = all_players[0]['id'],
            full_name = all_players[0]['full_name'],
            first_name = all_players[0]['first_name'],
            last_name = all_players[0]['last_name'],
            retired = all_players[0]['is_active'],
            current_team = teams.find_team_name_by_id(df_career_totals_regular_season['Team_ID'][0]),
            games_played = df_career_totals_regular_season['GP'][0],
            games_started = df_career_totals_regular_season['GS'][0],
            minutes_played = df_career_totals_regular_season['MIN'][0],
            field_goals_made = df_career_totals_regular_season['FGM'][0],
            field_goals_attempted = df_career_totals_regular_season['FGA'][0],
            field_goal_percentage = df_career_totals_regular_season['FG_PCT'][0],
            three_pointers_made = df_career_totals_regular_season['FG3M'][0],
            three_pointers_attempted = df_career_totals_regular_season['FG3A'][0],
            three_point_percentage = df_career_totals_regular_season['FG3_PCT'][0],
            free_throws_made = df_career_totals_regular_season['FTM'][0],
            free_throws_attempted = df_career_totals_regular_season['FTA'][0],
            free_throw_percentage = df_career_totals_regular_season['FT_PCT'][0],
            offensive_rebounds = df_career_totals_regular_season['OREB'][0],
            defensive_rebounds = df_career_totals_regular_season['DREB'][0],
            total_rebounds = df_career_totals_regular_season['REB'][0],
            assists = df_career_totals_regular_season['AST'][0],
            steals = df_career_totals_regular_season['STL'][0],
            blocks = df_career_totals_regular_season['BLK'][0],
            turnovers = df_career_totals_regular_season['TOV'][0],
            personal_fouls = df_career_totals_regular_season['PF'][0],
            points = df_career_totals_regular_season['PTS'][0]
        )

        db.session.add(player)
        db.session.commit()

        # for _, row in all_players.iterrows():
        #     player_id = row['id']

        #     player = Players(
        #         player_id=row['id'],
        #         full_name=row['full_name'],
        #         first_name=row['first_name'],
        #         last_name=row['last_name'],
        #         retired=row['is_active'],

        #         # nicknames=player_info.get_nicknames(player_id),
        #         # alive=player_info.get_alive(player_id),

        #         # birthdate=player_info.get_birthdate(player_id),
        #         # height=player_info.get_height(player_id),
        #         # weight=player_info.get_weight(player_id),
        #         # college=player_info.get_college(player_id),
        #         # country=player_info.get_country(player_id),
        #         # position=player_info.get_position(player_id),
        #         # current_team=player_info.get_current_team(player_id),
        #         # teams=player_info.get_teams(player_id),
        #         # draft_year=player_info.get_draft_year(player_id),
        #         # draft_round=player_info.get_draft_round(player_id),
        #         # draft_number=player_info.get_draft_number(player_id),
        #         # games_played=player_info.get_games_played(player_id),
        #         # games_started=player_info.get_games_started(player_id),
        #         # minutes_played=player_info.get_minutes_played(player_id),
        #         # field_goals_made=player_info.get_field_goals_made(player_id),
        #         # field_goals_attempted=player_info.get_field_goals_attempted(player_id),
        #         # field_goal_percentage=player_info.get_field_goal_percentage(player_id),
        #         # three_pointers_made=player_info.get_three_pointers_made(player_id),
        #         # three_pointers_attempted=player_info.get_three_pointers_attempted(player_id),
        #         # three_point_percentage=player_info.get_three_point_percentage(player_id),
        #         # two_pointers_made=player_info.get_two_pointers_made(player_id),
        #         # two_pointers_attempted=player_info.get_two_pointers_attempted(player_id),
        #         # two_point_percentage=player_info.get_two_point_percentage(player_id),
        #         # effective_field_goal_percentage=player_info.get_effective_field_goal_percentage(player_id),
        #         # free_throws_made=player_info.get_free_throws_made(player_id),
        #         # free_throws_attempted=player_info.get_free_throws_attempted(player_id),
        #         # free_throw_percentage=player_info.get_free_throw_percentage(player_id),
        #         # offensive_rebounds=player_info.get_offensive_rebounds(player_id),
        #         # defensive_rebounds=player_info.get_defensive_rebounds(player_id),
        #         # total_rebounds=player_info.get_total_rebounds(player_id),
        #         # assists=player_info.get_assists(player_id),
        #         # steals=player_info.get_steals(player_id),
        #         # blocks=player_info.get_blocks(player_id),
        #         # turnovers=player_info.get_turnovers(player_id),
        #         # personal_fouls=player_info.get_personal_fouls(player_id),
        #         # points=player_info.get_points(player_id)
        #     )

if __name__ == '__main__':
    fetch_players_data()