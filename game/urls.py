from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('/match-card/', views.match_card, name='game.match_card'),
    path('/nickname/', views.nickname, name='game.nickname'),
    path('/whoislate/', views.whoislate, name='game.whoislate'),
]
