from django.shortcuts import render
from .models import Event


# Create your views here.
def all_events(request):
    """ A view to show all events """

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
