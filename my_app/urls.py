from django.urls import path
from .views import *
urlpatterns = [
    path('',Home_page,name="home"),
]