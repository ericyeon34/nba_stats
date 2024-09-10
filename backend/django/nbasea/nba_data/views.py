# from django.shortcuts import render, get_object_or_404
from .models import Players
from django.views import generic
from django.urls import reverse

class PlayerList(generic.ListView):
    model = Players
    template_name = 'nba_data/player_list.html'
    context_object_name = 'players'

    def get_queryset(self):
        return Players.objects.all()

class PlayerDetail(generic.DetailView):
    model = Players
    template_name = 'nba_data/player_detail.html'
    context_object_name = 'player'