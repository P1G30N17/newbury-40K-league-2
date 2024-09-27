# Generated by Django 5.1.1 on 2024-09-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='games_played',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='league_points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='victory_points_tally',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='faction',
            field=models.CharField(max_length=50),
        ),
    ]