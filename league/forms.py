from django import forms
from .models import Player


class SubmitResultsForm(forms.ModelForm):
    player_vp = forms.IntegerField()

    class Meta:
        model = Player
        fields = ['player_vp',]