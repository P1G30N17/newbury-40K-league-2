from django.shortcuts import render, HttpResponse, redirect
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
    model = models.Player
    fields = ['name', 'faction', 'games_played', 'league_points', 'victory_points_tally']

class RegisterView(LoginRequiredMixin, CreateView):
    model = models.Player
    fields = ['name', 'faction']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlayerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Player
    fields = ['name', 'faction']

    def test_func(self):
        player = self.get_object()
        return self.request.user == player.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Player
    success_url = reverse_lazy('home')

    def test_func(self):
        player = self.get_object()
        return self.request.user == player.user

def update(request, id):
  player = Player.objects.get(id=id)
  template_name = "league/submitresults.html"
  context = {
    'player': player,
  }
  return render(request, "league/submitresults.html", context)

def submit(request, id):
  results = request.POST['results']
  player = Player.objects.get(id=id)
  player.victory_points_tally += int(results)
  player.games_played += 1
  player.save()
  return HttpResponseRedirect(reverse('home'))

    
def about(request):
    return render(request, "league/about.html", {'title': 'About the Newbury 40K League'})
