### credits #5 (see README.md credits section) ###
from django.shortcuts import render, redirect
from django.urls import reverse

import stripe
import os


stripe.api_key = os.getenv('STRIPE_API_KEY', '')


# Create your views here.
def buy_premium(request):
    """
    A view to render the buy premium page. 
    Only works if user is logged in 
    and doesn't have premium already.
    """

    if not request.user.is_authenticated:
        return redirect('/accounts/signup/')

    else:
        current_user = request.user

        if current_user.premium:
            return render(request, 'premium/already_premium.html')

        else:
            return render(request, 'premium/premium.html')


def charge(request):
    """
    Process stripe payment for premium membership
    """

    current_user = request.user

    if request.method == 'POST':
        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description="Premium membership"
            )

        current_user.premium = True
        current_user.save()

    return redirect(reverse('success'))


def successMsg(request):
    """
    Render the Stripe payment successful view.
    """

    if not request.user.is_authenticated:
        return redirect('/accounts/signup/')

    else:
        if not request.user.premium:
            return redirect('/premium/')

        else:
            return render(request, 'premium/payment_success.html')
