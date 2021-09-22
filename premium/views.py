from django.shortcuts import render


# Create your views here.
def premium(request):
    """ A view to return the premium page """

    return render(request, 'premium/premium.html')
