from django.contrib import admin
from django.urls import path
from . import views
from events.views import all_events

urlpatterns = [
    path("events/", all_events, name="all_events"),
    path("profile/", views.profile, name="profile"),
    path('', views.index, name='home'),
]
