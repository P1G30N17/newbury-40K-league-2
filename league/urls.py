from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlayerListView.as_view(), name="home"),
    path('player/<int:pk>/', views.PlayerDetailView.as_view(), name="player-detail"),
    path('player/register/', views.RegisterView.as_view(), name="player-register"),
    path('player/<int:pk>/update', views.PlayerUpdateView.as_view(), name="player-update"),
    path('player/<int:pk>/delete', views.PlayerDeleteView.as_view(), name="player-delete"),
    # allow this path once user authentication is added to view
    # path('player/<int:pk>/submitresults', views.SubmitResultsView.as_view(), name="submit-results"),
    path('player/submitresults', views.SubmitResultsView.as_view(), name="submit-results"),
    path('about/', views.about, name="about"),
]