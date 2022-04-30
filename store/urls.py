from django.contrib import admin
from django.urls import path
from django.urls import path
from .views import Index
from .views import signup,login
from . import views

urlpatterns = [
    path('',Index.as_view(),name='homepage'),
    path('signup', signup),
    path('login',login)
]
