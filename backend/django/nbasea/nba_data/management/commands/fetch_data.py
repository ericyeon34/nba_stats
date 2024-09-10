from django.core.management.base import BaseCommand
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats
from nba_data.models import Players
import pandas as pd
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Fetches player data from NBA API and populates the database'

    def handle(self, *args, **kwargs):
        self.fetch_players_data()

    def fetch_players_data(self):
        all_players = players.get_players()
        for player in all_players:
            try:
                career = playercareerstats.PlayerCareerStats(player_id=player['id']).get_dict()['resultSets']
                dict_career_totals_regular_season = next((item for item in career if item['name'] == 'CareerTotalsRegularSeason'), None)

                if dict_career_totals_regular_season:
                    df_career_totals_regular_season = pd.DataFrame(dict_career_totals_regular_season['rowSet'], columns=dict_career_totals_regular_season['headers'])
                    
                    if df_career_totals_regular_season.empty:
                        continue

                    existing_player = Players.objects.filter(player_id=player['id']).first()

                    if existing_player:
                        # Update player logic here (if needed)
                        continue
                    else:
                        # Add new player to the database
                        new_player = Players(
                            player_id=player['id'],
                            full_name=player['full_name'],
                            first_name=player['first_name'],
                            last_name=player['last_name'],
                            retired=player['is_active'],
                            # current_team=teams.find_team_name_by_id(df_career_totals_regular_season['Team_ID'][0]),
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
                        new_player.save()

                        self.stdout.write(self.style.SUCCESS(f"Player {player['full_name']} added to database."))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error adding player {player['full_name']} to database: {str(e)}"))
                continue
