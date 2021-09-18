from django.urls import path
from . import views
from weather.views import daily_forecast, hourly_forecast

urlpatterns = [
    path("<event_id>/hourlyforecast/", hourly_forecast, name="hourly_forecast"),
    path("<event_id>/dailyforecast/", daily_forecast, name="daily_forecast"),
    path('<event_id>/', views.single_event, name='single_event'),
    path('', views.all_events, name='events'),
]
