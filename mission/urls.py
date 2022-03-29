from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('',views.mission, name='mission'),#url mapping with view 
]