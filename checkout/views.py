from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HzoLzDW5x11TxMr7sKfFIf1p1nhSBwCpudacWniDbHlK16hKZ91N9Wb9E8rRC5VMvqkGZb99QWb8IwULa0xeoiJ00vs7sirct',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
