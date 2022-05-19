from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # url mapping with view
    path('vacancy/<int:id>', views.vacancy_detail, name='vacancy_detail'),  # url mapping with view
    path('tender/<int:id>', views.tender_detail, name='tender_detail'),  # url mapping with view
    path('<int:id>', views.detail, name='detail'),  # url mapping with view
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('search', views.search, name='search')
]
