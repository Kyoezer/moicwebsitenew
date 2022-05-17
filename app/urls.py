"""creative_index URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('indexapp.urls')),
    path('background/', include('background.urls')),
    path('mission/', include('mission.urls')),
    path('organogram/', include('organogram.urls')),
    path('whoiswho/', include('whoiswho.urls')),
    path('department/', include('department.urls')),
    path('annual/', include('annual.urls')),
    path('publication/', include('publication.urls')),
    path('contact/', include('contact.urls')),
    path('information/', include('information.urls')),
    path('search/', include('search.urls')),
    path('moic_admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
