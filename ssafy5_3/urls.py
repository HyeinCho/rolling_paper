from django.urls import path
from . import views

app_name = 'ssafy5-3'
urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.messages, name='messages'),
    path('collegues/', views.collegues, name='collegues'),
    path('greetings/', views.messages, name='greetings'),
    path('coin/', views.load_coin, name='coin'),
    path('loadmessages/', views.load_messages, name='loadmessages'),
    path('openmessage/<int:id>/', views.open_message, name='openMessage'),
    path('insertcoin/<int:coin_num>/', views.insert_coin, name='insertCoin'),
]
