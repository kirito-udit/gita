from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name = 'home'),
   path('A1',views.a1, name='a1'),
]
