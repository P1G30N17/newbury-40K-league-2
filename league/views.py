from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from . import models

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
    fields = ['name', 'faction']

class RegisterView(LoginRequiredMixin, CreateView):
    model = models.Player
    fields = ['name', 'faction']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class PlayerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Player
    fields = ['name', 'faction']

    def test_func(self):
        player = self.get_object()
        return self.request.user == player.user_id

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class PlayerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Player
    success_url = reverse_lazy('home')

    def test_func(self):
        player = self.get_object()
        return self.request.user == player.user_id
        
def about(request):
    return render(request, "league/about.html", {'title': 'About the Newbury 40K League'})
