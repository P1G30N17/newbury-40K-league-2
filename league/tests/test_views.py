from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from league.models import Player

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
    
        self.client = Client()
        self.list_url = reverse('home')
        self.detail_url = reverse('player-detail', kwargs={"pk": 1})
        self.register_url = reverse('player-register')
        self.delete_url = reverse('player-delete', kwargs={"pk": 1})

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'league/home.html')

    def test_project_player_detail_GET(self):
        self.player = Player(user=self.user, name="test-player",
                         email="test@test.com", faction="test-faction",
                         games_played="1", league_points="1",
                         victory_points_tally="99")
        self.player.save()

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'league/player_detail.html')

    def test_project_register_POST(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 302)
        Player.objects.create(user=self.user, name='test-player', faction='test-faction')
        self.assertEqual(Player.objects.last().name, 'test-player')
        self.assertEqual(Player.objects.last().faction, 'test-faction')

    # def test_project_DELETE_deletes_player(self):
    #     self.player = Player(user=self.user, name="test-player",
    #                      email="test@test.com", faction="test-faction",
    #                      games_played="1", league_points="1",
    #                      victory_points_tally="99")
    #     self.player.save()

    #     response = Player.delete(self.delete_url)
    #     with self.assertRaises(self.player.DoesNotExist):
    #         self.player.refresh_from_db()
        # self.assertEqual(response.status_code, 204)
        # self.assertEqual(response.status_code, 204)
        # self.assertEqual(self.player.count(), 0)