from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerListView.as_view(), name="home"),
    # link to each individual player /player/1
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name="player-detail"),
    path('player/register/', views.RegisterView.as_view(), name="player-register"),
    path('player/<int:pk>/update', views.PlayerUpdateView.as_view(), name="player-update"),
    path('about/', views.about, name="about"),
]