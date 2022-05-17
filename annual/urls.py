from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('', views.annual1, name='annual1'),
    path('annual2/', views.annual2, name='annual2'),
    path('annual3/', views.annual3, name='annual3')#url mapping with view
]