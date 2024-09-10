from django.test import TestCase
from django.urls import reverse
from .models import Players

# Create your tests here.

class PlayerModelTest(TestCase):
    def setUp(self):
        self.player = Players.objects.create(
            player_id=1,
            full_name='Test Player',
            first_name='Test',
            last_name='Player',
            retired=False,
            # current_team='Test Team',
            games_played=1,
            games_started=1,
            minutes_played=1,
            field_goals_made=1,
            field_goals_attempted=1,
            field_goal_percentage=1.0,
            three_pointers_made=1,
            three_pointers_attempted=1,
            three_point_percentage=1.0,
            free_throws_made=1,
            free_throws_attempted=1,
            free_throw_percentage=1.0,
            offensive_rebounds=1,
            defensive_rebounds=1,
            total_rebounds=1,
            assists=1,
            steals=1,
            blocks=1,
            turnovers=1,
            personal_fouls=1,
            points=1
        )

        def test_player_creation(self):
            """Test the player model creation."""
            self.assertTrue(isinstance(self.player, Players))
            self.assertEqual(self.player.__str__(), self.player.full_name)
        
class PlayerListViewTest(TestCase):
    def setUp(self):
        Players.objects.create(
            player_id=1,
            full_name='Test Player',
            first_name='Test',
            last_name='Player',
            retired=False,
            # current_team='Test Team',
            games_played=1,
            games_started=1,
            minutes_played=1,
            field_goals_made=1,
            field_goals_attempted=1,
            field_goal_percentage=1.0,
            three_pointers_made=1,
            three_pointers_attempted=1,
            three_point_percentage=1.0,
            free_throws_made=1,
            free_throws_attempted=1,
            free_throw_percentage=1.0,
            offensive_rebounds=1,
            defensive_rebounds=1,
            total_rebounds=1,
            assists=1,
            steals=1,
            blocks=1,
            turnovers=1,
            personal_fouls=1,
            points=1
        )

        Players.objects.create(
            player_id=2,
            full_name='Test Player 2',
            first_name='Test',
            last_name='Player 2',
            retired=False,
            # current_team='Test Team 2',
            games_played=2,
            games_started=2,
            minutes_played=2,
            field_goals_made=2,
            field_goals_attempted=2,
            field_goal_percentage=2.0,
            three_pointers_made=2,
            three_pointers_attempted=2,
            three_point_percentage=2.0,
            free_throws_made=2,
            free_throws_attempted=2,
            free_throw_percentage=2.0,
            offensive_rebounds=2,
            defensive_rebounds=2,
            total_rebounds=2,
            assists=2,
            steals=2,
            blocks=2,
            turnovers=2,
            personal_fouls=2,
            points=2
        )

    def test_player_list_view(self):
        """Test the player list view."""
        response = self.client.get(reverse('nba_data:player_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Player')
        self.assertContains(response, 'Test Player 2')
        self.assertTemplateUsed(response, 'nba_data/player_list.html')

class PlayerDetailViewTest(TestCase):
    def setUp(self):
        self.player = Players.objects.create(
            player_id=1,
            full_name='Test Player',
            first_name='Test',
            last_name='Player',
            retired=False,
            # current_team='Test Team',
            games_played=1,
            games_started=1,
            minutes_played=1,
            field_goals_made=1,
            field_goals_attempted=1,
            field_goal_percentage=1.0,
            three_pointers_made=1,
            three_pointers_attempted=1,
            three_point_percentage=1.0,
            free_throws_made=1,
            free_throws_attempted=1,
            free_throw_percentage=1.0,
            offensive_rebounds=1,
            defensive_rebounds=1,
            total_rebounds=1,
            assists=1,
            steals=1,
            blocks=1,
            turnovers=1,
            personal_fouls=1,
            points=1
        )

    def test_player_detail_view(self):
        """Test the player detail view."""
        response = self.client.get(reverse('nba_data:player_detail', args=[self.player.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Player')
        self.assertTemplateUsed(response, 'nba_data/player_detail.html')

from django.core.management import call_command
from unittest.mock import patch
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

class FetchDataCommandTest(TestCase):

    @patch('nba_api.stats.static.players.get_players') # Mocks the get_players method from the players module
    @patch('nba_api.stats.endpoints.playercareerstats.PlayerCareerStats.get_dict') # Mocks the get_dict method from the PlayerCareerStats class

    def test_fetch_players_data(self, mock_get_dict, mock_get_players):
        """Test that the fetch_data command populates the database correctly"""

        # Mock the return value of the get_players method
        mock_get_players.return_value = [
            {
                'id': 1,
                'full_name': 'Test Player',
                'first_name': 'Test',
                'last_name': 'Player',
                'is_active': False
            },
            {
                'id': 2,
                'full_name': 'Test Player 2',
                'first_name': 'Test',
                'last_name': 'Player 2',
                'is_active': False
            }
        ]

        # Mock the return value of the get_dict method
        mock_get_dict.return_value = {
            'resultSets': [{
                'name': 'CareerTotalsRegularSeason',
                'headers': ['GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'],
                'rowSet': [
                    [1, 1, 1, 1, 1, 1.0, 1, 1, 1.0, 1, 1, 1.0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1.0, 1, 1, 1.0, 1, 1, 1.0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            }]
        }

        # Run the fetch_data command
        call_command('fetch_data')

        # Check that the database has been populated correctly
        self.assertEqual(Players.objects.count(), 2)

        # Check that the first player has been added correctly
        test_player1 = Players.objects.get(player_id=1)
        self.assertEqual(test_player1.full_name, 'Test Player')
        self.assertEqual(test_player1.first_name, 'Test')
        self.assertEqual(test_player1.last_name, 'Player')
        self.assertEqual(test_player1.retired, False)
        # self.assertEqual(test_player1.current_team, None)
        self.assertEqual(test_player1.games_played, 1)
        self.assertEqual(test_player1.games_started, 1)
        self.assertEqual(test_player1.minutes_played, 1)
        self.assertEqual(test_player1.field_goals_made, 1)
        self.assertEqual(test_player1.field_goals_attempted, 1)
        self.assertEqual(test_player1.field_goal_percentage, 1.0)
        self.assertEqual(test_player1.three_pointers_made, 1)
        self.assertEqual(test_player1.three_pointers_attempted, 1)
        self.assertEqual(test_player1.three_point_percentage, 1.0)
        self.assertEqual(test_player1.free_throws_made, 1)
        self.assertEqual(test_player1.free_throws_attempted, 1)
        self.assertEqual(test_player1.free_throw_percentage, 1.0)
        self.assertEqual(test_player1.offensive_rebounds, 1)
        self.assertEqual(test_player1.defensive_rebounds, 1)
        self.assertEqual(test_player1.total_rebounds, 1)
        self.assertEqual(test_player1.assists, 1)
        self.assertEqual(test_player1.steals, 1)
        self.assertEqual(test_player1.blocks, 1)
        self.assertEqual(test_player1.turnovers, 1)
        self.assertEqual(test_player1.personal_fouls, 1)
        self.assertEqual(test_player1.points, 1)

        # Check that the second player has been added correctly
        test_player2 = Players.objects.get(player_id=2)
        self.assertEqual(test_player2.full_name, 'Test Player 2')
        self.assertEqual(test_player2.first_name, 'Test')
        self.assertEqual(test_player2.last_name, 'Player 2')
        self.assertEqual(test_player2.retired, False)
        # self.assertEqual(test_player2.current_team, None)
        self.assertEqual(test_player2.games_played, 1)
        self.assertEqual(test_player2.games_started, 1)
        self.assertEqual(test_player2.minutes_played, 1)
        self.assertEqual(test_player2.field_goals_made, 1)
        self.assertEqual(test_player2.field_goals_attempted, 1)
        self.assertEqual(test_player2.field_goal_percentage, 1.0)
        self.assertEqual(test_player2.three_pointers_made, 1)
        self.assertEqual(test_player2.three_pointers_attempted, 1)
        self.assertEqual(test_player2.three_point_percentage, 1.0)
        self.assertEqual(test_player2.free_throws_made, 1)
        self.assertEqual(test_player2.free_throws_attempted, 1)
        self.assertEqual(test_player2.free_throw_percentage, 1.0)
        self.assertEqual(test_player2.offensive_rebounds, 1)
        self.assertEqual(test_player2.defensive_rebounds, 1)
        self.assertEqual(test_player2.total_rebounds, 1)
        self.assertEqual(test_player2.assists, 1)
        self.assertEqual(test_player2.steals, 1)
        self.assertEqual(test_player2.blocks, 1)
        self.assertEqual(test_player2.turnovers, 1)
        self.assertEqual(test_player2.personal_fouls, 1)
        self.assertEqual(test_player2.points, 1)