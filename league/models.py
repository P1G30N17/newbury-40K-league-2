from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    faction = models.CharField(max_length=50)
    games_played = models.PositiveIntegerField(default=0)
    league_points = models.PositiveIntegerField(default=0)
    victory_points_tally = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse("player-detail", kwargs={"pk": self.pk})

    def update_stats(self, player_score):
        self.games_played += 1
        self.victory_points_tally += player_score
        self.save

    def __str__(self):
        return self.name

    
class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_vp = models.PositiveIntegerField(default=0)

    def submit_score(self, player_score):
        self.player.update_stats(self.player_vp)
        super().save()

    def __str__(self):
        return f"Results submitted successfully"
    
