from django.urls import path
from . import views

app_name = 'ssafy5_3'
urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.messages, name='messages'),
    path('collegues/', views.collegues, name='collegues'),
    path('greetings/', views.greetings, name='greetings'),
]
