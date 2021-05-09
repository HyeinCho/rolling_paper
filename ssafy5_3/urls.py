from django.urls import path
from . import views

app_name = 'ssafy5_3'
urlpatterns = [
    path('', views.index, name='ssafy5_3.index'),
    path('messages/', views.messages, name='ssafy5_3.messages'),
    path('collegues/', views.collegues, name='ssafy5_3.collegues'),
    path('greetings/', views.messages, name='ssafy5_3.greetings'),
]
