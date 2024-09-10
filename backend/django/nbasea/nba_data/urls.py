from django.urls import path
from . import views

app_name = 'nba_data'
urlpatterns = [
    # # ex: /nba_data/players/
    # path('players/', views.players, name='players'),
    # # ex: /nba_data/players/5/
    # path('players/<int:player_id>/', views.player, name='player'),
    path("", views.PlayerList.as_view(), name="player_list"),
    path("<int:pk>/", views.PlayerDetail.as_view(), name="player_detail"),
]