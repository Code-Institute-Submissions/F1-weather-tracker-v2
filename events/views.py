from django.shortcuts import render, get_object_or_404
from .models import Event


# Create your views here.
def all_events(request):
    """
    A view to show all events 
    (render the formula 1 calendar)
    """

    russia = Event.objects.get(event_id=2021001)
    turkey = Event.objects.get(event_id=2021002)
    us = Event.objects.get(event_id=2021003)
    mexico = Event.objects.get(event_id=2021004)
    brazil = Event.objects.get(event_id=2021005)
    sa = Event.objects.get(event_id=2021006)
    uae = Event.objects.get(event_id=2021007)

    context = {
        'russia': russia,
        'turkey': turkey,
        'us': us,
        'mexico': mexico,
        'brazil': brazil,
        'sa': sa,
        'uae': uae,
    }

    return render(request, 'events/events.html', context)


def single_event(request, event_id):
    """
    A view to show individual event weather options 
    for the previously selected calendar event
    """

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/single_event.html', context)
