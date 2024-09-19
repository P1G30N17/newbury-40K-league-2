from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    faction = models.TextField()

    def __str__(self):
        return self.name

