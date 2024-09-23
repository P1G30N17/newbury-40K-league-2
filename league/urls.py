from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerListView.as_view(), name="home"),
    # link to each indicidual player /player/1
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name="player-detail"),
    path('about/', views.about, name="about"),
]