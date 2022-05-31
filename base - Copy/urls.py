from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    # url mapping with view
]
