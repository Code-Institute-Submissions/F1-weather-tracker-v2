"""f1_weather_tracker URL Configuration

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
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ### credits #6 (see README.md credits section) ###
    path("favicon.ico", RedirectView.as_view(
        url=staticfiles_storage.url("favicon.ico")),),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('events/', include('events.urls')),
    path('premium/', include('premium.urls')),
]

# custom error handlers

handler400 = 'f1_weather_tracker.views.error_400'
handler403 = 'f1_weather_tracker.views.error_403'
handler404 = 'f1_weather_tracker.views.error_404'
handler500 = 'f1_weather_tracker.views.error_500'
