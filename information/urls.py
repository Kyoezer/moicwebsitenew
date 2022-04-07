from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('moicofficails/',views.moicofficials, name='moicofficials'),
    path('download/',views.download, name='download'),
    path('hrdecisions/',views.hrdecisions, name='hrdecisions'),
    path('rstaservices/',views.rsrstaservices, name='rstaservices'),#url mapping with view 
]