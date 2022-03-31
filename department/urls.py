from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('doat/',views.doat, name='doat'),
    path('ditt/',views.ditt, name='ditt'),
    path('doim/',views.doim, name='doim'),
    path('rsta/',views.rsta, name='rsta'),#url mapping with view 
]