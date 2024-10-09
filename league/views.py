from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.template import loader
from django.http import HttpResponseRedirect

from . import models
from .models import Player

# Create your views here.
def home(request):
    players = models.Player.objects.all()
    context = {
        'players': players
    }
    return render(request, "league/home.html", context)

class PlayerListView(ListView):
    model = models.Player
    template_name = 'league/home.html'
    context_object_name = 'players'

class PlayerDetailView(DetailView):
    """
    Displays an individual player's details
    """
    model = models.Player
    fields = ['name', 'faction', 'games_played', 'league_points', 'victory_points_tally']

class RegisterView(LoginRequiredMixin, CreateView):
    """
    Renders the league registration form for logged in user
    """
    model = models.Player
    fields = ['name', 'faction']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlayerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows a logged in user to update their player profile
    """
    model = models.Player
    fields = ['name', 'faction']

    def test_func(self):
        player = self.get_object()
        return self.request.user == player.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows a logged in user to delete their player profile
    """
    model = models.Player
    success_url = reverse_lazy('home')

    def test_func(self):
        player = self.get_object()
        return self.request.user == player.user

def update(request, pk):
  """
  Renders the players score submission page
  """
  player = Player.objects.get(pk=pk)  
  template_name = "league/submitresults.html"
  context = {
    'player': player,
  }
  return render(request, "league/submitresults.html", context)

def submit(request, pk):
  """
  Handles the score submission post and updates Player model accordingly
  """  
  results = request.POST['results']
  player = Player.objects.get(pk=pk)
  player.victory_points_tally += int(results)
  player.games_played += 1
  if request.POST.get('victory') is not None:
    player.league_points += 2
  else:
    player.league_points += 1
  player.save()
  messages.success(request, f"{player.name}, your results have been submitted successfully!")
  return HttpResponseRedirect(reverse('home'))

    
def about(request):
    """
    Renders the About page
    """
    return render(request, "league/about.html", {'title': 'About the Newbury 40K League'})
