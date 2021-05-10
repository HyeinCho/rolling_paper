from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('stage1/', views.stage1, name='stage1'),
    path('stage2/', views.stage2, name='stage2'),
    path('stage2/<int:pk>/', views.card_flip, name='card_flip'),
    path('stage2/get_hint/<int:pk>/', views.getHint, name='getHint'),
    path('stage2/balance/<int:pk>/', views.balance_game, name='balance_game'),
    path('stage2/balance/<int:game_pk>/<int:choice_pk>/', views.choose_one, name='choose_one'),
    path('stage3/', views.stage3, name='stage3'),
    path('bonus/', views.bonus, name='bonus'),
    path('bonus/<int:chat_id>/chat/', views.getChatMessage, name='chat'),
    path('rewards/', views.rewards, name='rewards'),
]
