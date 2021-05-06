from django.urls import path
from . import views

app_name = 'game'
urlpatterns = [
    path('stage1/', views.stage1, name='stage1'),
    path('stage2/', views.stage2, name='stage2'),
    path('stage3/', views.stage3, name='stage3'),
    path('bonus/', views.bonus, name='bonus'),
    path('bonus/<int:chat_id>/chat/', views.getChatMessage, name='chat'),
    path('rewards/', views.rewards, name='rewards'),
]
