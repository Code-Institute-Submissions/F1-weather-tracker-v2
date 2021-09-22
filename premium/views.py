from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
#from django.http import JsonResponse
#from accounts.models import CustomUser
#from django.contrib.auth.models import User

import stripe
import os


stripe.api_key = os.getenv('STRIPE_API_KEY', '')


# Create your views here.
def buy_premium(request):
    """ A view to return the buy premium page """

    current_user = request.user
    print(current_user.email)

    if current_user.premium:
        return render(request, 'premium/already_premium.html')

    else:
        return render(request, 'premium/premium.html')


def charge(request):
    """ Process stripe payment for premium membership """

    current_user = request.user

    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            source=request.POST['stripeToken']
            )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description="Donation"
            )

        current_user.premium = True
        current_user.save()

    return redirect(reverse('success'))


def successMsg(request):
    """ Stipe payment successful view """

    return render(request, 'premium/payment_success.html')
