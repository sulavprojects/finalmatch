from importlib.resources import path
from operator import index
from .views import *
from django.urls import path

urlpatterns = [
    path('' , main , name="home"),
    
]