from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('policies/',views.policies, name='policies'),
    path('acts/',views.acts, name='acts'),
    path('rules/',views.rules, name='rules'),
    path('guidelines/',views.guidelines, name='guidelines'),
    path('reports/',views.reports, name='reports'),
    path('statistics/',views.statistics, name='statistics'), #url mapping with view 
]