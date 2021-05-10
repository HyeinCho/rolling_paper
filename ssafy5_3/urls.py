from django.urls import path
from . import views

app_name = 'ssafy5_3'
urlpatterns = [
    path('', views.index, name='ssafy5_3.index'),
    path('messages/', views.messages, name='ssafy5_3.messages'),
    path('collegues/', views.collegues, name='ssafy5_3.collegues'),
    path('greetings/', views.messages, name='ssafy5_3.greetings'),
    path('coin/', views.load_coin, name='coin'),
    path('messages/', views.load_messages, name='messages'),
    path('openmessage/<int:id>/', views.open_message, name='openMessage'),
    path('insertcoin/<int:coin_num>/', views.insert_coin, name='insertCoin'),
]
