from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('',views.whoiswho, name='whoiswho'),#url mapping with view 
]