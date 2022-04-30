from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import index,signup,login
from . import views

urlpatterns = [
    path('',index,name='homepage'),
    path('signup', signup),
    path('login',login)
]
