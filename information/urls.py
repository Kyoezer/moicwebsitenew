from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('moicofficails/', views.moicofficials, name='moicofficials'),
    path('download/', views.download, name='download'),
    path('hrdecisions/', views.hrdecision, name='hrdecisions'),
    path('rstaservices/', views.rsrstaservices, name='rstaservices'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    # url mapping with view
]
