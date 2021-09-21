from django.shortcuts import render, get_object_or_404
from events.models import Event
from .models import Schedule


# Create your views here.
def daily_forecast(request, event_id):
    """ A view to show daily weather forecast data """

    event = get_object_or_404(Event, pk=event_id)
    schedule = get_object_or_404(Schedule, pk=event_id)

    context = {
        'event': event,
        'schedule': schedule,
    }

    return render(request, 'weather/daily_forecast.html', context)


def hourly_forecast(request, event_id):
    """ A view to show hourly weather forecast data """

    event = get_object_or_404(Event, pk=event_id)
    schedule = get_object_or_404(Schedule, pk=event_id)

    context = {
        'event': event,
        'schedule': schedule,
    }

    return render(request, 'weather/hourly_forecast.html', context)
