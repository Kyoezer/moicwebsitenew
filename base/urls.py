from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('',views.base, name='base'),#url mapping with view
]