from unicodedata import name
from django.urls import path
from.import views


urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('mail_letter/', views.mail_letter, name='mail_letter')
    #url mapping with view
]