from django.shortcuts import render, HttpResponse
from . import models

players = [
    {
        'name': 'James King',
        'faction': 'Tyranids',
        'league_points': '237',
        'games_played': '2',
        'league_position': '4'
    },
    {
        'name': 'Jimmy King',
        'faction': 'Space Marines',
        'league_points': '289',
        'games_played': '4',
        'league_position': '2'
    },
    {
        'name': 'Peter Scott',
        'faction': 'Grey Knights',
        'league_points': '301',
        'games_played': '4',
        'league_position': '1'
    },
    {
        'name': 'Jack White',
        'faction': 'Tyranids',
        'league_points': '299',
        'games_played': '3',
        'league_position': '3'
    },
]

# Create your views here.
def home(request):
    players = models.Player.objects.all()
    context = {
        'players': players
    }
    return render(request, "league/home.html", context)

def about(request):
    return render(request, "league/about.html", {'title': 'About the Newbury 40K League'})
