from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class RegisterView(LoginRequiredMixin, CreateView):
    model = models.Player
    fields = ['name', 'faction']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)
        

def about(request):
    return render(request, "league/about.html", {'title': 'About the Newbury 40K League'})
