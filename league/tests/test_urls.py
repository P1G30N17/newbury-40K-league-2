from django.test import SimpleTestCase
from django.urls import reverse, resolve
from league.views import home, PlayerListView, PlayerDetailView, RegisterView, PlayerUpdateView, PlayerDeleteView, update, submit, about

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, PlayerListView)

    def test_player_detail_url_resolves(self):
        url = reverse('player-detail', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PlayerDetailView)

    def test_player_register_url_resolves(self):
        url = reverse('player-register')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_player_update_url_resolves(self):
        url = reverse('player-update', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PlayerUpdateView)

    def test_player_delete_url_resolves(self):
        url = reverse('player-delete', args=['1'])
        self.assertEqual(resolve(url).func.view_class, PlayerDeleteView)


    def test_player_submit_results_url_resolves(self):
        url = reverse('update', args=['1'])
        self.assertEqual(resolve(url).func, update)

    def test_player_submit_url_resolves(self):
        url = reverse('submit', args=['1'])
        self.assertEqual(resolve(url).func, submit)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)