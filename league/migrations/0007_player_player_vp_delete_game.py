# Generated by Django 5.1.1 on 2024-10-02 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_remove_player_player_vp_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='player_vp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
