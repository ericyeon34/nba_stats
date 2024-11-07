# from django.shortcuts import render, get_object_or_404
from .models import Player
from django.views import generic
from django.urls import reverse

class PlayerList(generic.ListView):
    model = Player
    template_name = 'nba_data/player_list.html'
    context_object_name = 'players'
    # paginate_by = 10 # Number of players per page

    def get_queryset(self):
        return Player.objects.all().order_by('last_name')

class PlayerDetail(generic.DetailView):
    model = Player
    template_name = 'nba_data/player_detail.html'
    context_object_name = 'player'