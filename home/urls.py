from importlib.resources import path
from operator import index
from .views import *
from django.urls import path

urlpatterns = [
    path('' , main , name="home"),
    path('allfonts' , allfonts , name="allfonts"),
    path('<slug:slug>/' , fonts_details , name="fonts_details"),
    
]