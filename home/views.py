from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    """ A view to return the home page """

    return render(request, 'home/index.html')


def profile(request):
    """ A view to render the profile page """

    if not request.user.is_authenticated:
        return redirect('/accounts/signup/')

    else:
        return render(request, 'home/profile.html')
