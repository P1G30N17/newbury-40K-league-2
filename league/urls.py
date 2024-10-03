from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerListView.as_view(), name="home"),
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name="player-detail"),
    path('player/register/', views.RegisterView.as_view(), name="player-register"),
    path('player/<int:pk>/update', views.PlayerUpdateView.as_view(), name="player-update"),
    path('player/<int:pk>/delete', views.PlayerDeleteView.as_view(), name="player-delete"),
    path('player/<int:pk>/submitresults', views.submit_results, name="submit-results"),
    path('about/', views.about, name="about"),
]