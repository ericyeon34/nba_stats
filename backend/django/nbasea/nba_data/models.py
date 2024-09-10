from django.db import models

# Create your models here.

class Players(models.Model):
    player_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    retired = models.BooleanField()
    # current_team = models.CharField(max_length=50, null=True)

    games_played = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    minutes_played = models.IntegerField(null=True)
    field_goals_made = models.IntegerField(null=True)
    field_goals_attempted = models.IntegerField(null=True)
    field_goal_percentage = models.FloatField(null=True)
    three_pointers_made = models.IntegerField(null=True)
    three_pointers_attempted = models.IntegerField(null=True)
    three_point_percentage = models.FloatField(null=True)
    free_throws_made = models.IntegerField(null=True)
    free_throws_attempted = models.IntegerField(null=True)
    free_throw_percentage = models.FloatField(null=True)
    offensive_rebounds = models.IntegerField(null=True)
    defensive_rebounds = models.IntegerField(null=True)
    total_rebounds = models.IntegerField(null=True)
    assists = models.IntegerField(null=True)
    steals = models.IntegerField(null=True)
    blocks = models.IntegerField(null=True)
    turnovers = models.IntegerField(null=True)
    personal_fouls = models.IntegerField(null=True)
    points = models.IntegerField(null=True)

    # def to_dict(self):
    #     """
    #     Convert the object to a dictionary.
    #     """
    #     return {
    #         'player_id': self.player_id,
    #         'full_name': self.full_name,
    #         'first_name': self.first_name,
    #         'last_name': self.last_name,
    #         'retired': self.retired,
    #         'current_team': self.current_team,

    #         'games_played': self.games_played,
    #         'games_started': self.games_started,
    #         'minutes_played': self.minutes_played,
    #         'field_goals_made': self.field_goals_made,
    #         'field_goals_attempted': self.field_goals_attempted,
    #         'field_goal_percentage': self.field_goal_percentage,
    #         'three_pointers_made': self.three_pointers_made,
    #         'three_pointers_attempted': self.three_pointers_attempted,
    #         'three_point_percentage': self.three_point_percentage,
    #         'free_throws_made': self.free_throws_made,
    #         'free_throws_attempted': self.free_throws_attempted,
    #         'free_throw_percentage': self.free_throw_percentage,
    #         'offensive_rebounds': self.offensive_rebounds,
    #         'defensive_rebounds': self.defensive_rebounds,
    #         'total_rebounds': self.total_rebounds,
    #         'assists': self.assists,
    #         'steals': self.steals,
    #         'blocks': self.blocks,
    #         'turnovers': self.turnovers,
    #         'personal_fouls': self.personal_fouls,
    #         'points': self.points
    #     }

    class Meta:
        db_table = 'players'