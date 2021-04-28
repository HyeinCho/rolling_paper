from django.urls import path
from . import views

app_name = 'class3'
urlpatterns = [
    path('', views.index, name='class3.index'),
    path('/students/', views.info_students, name='class3.info_students'),
]
