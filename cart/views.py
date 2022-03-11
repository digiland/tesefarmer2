
from django.shortcuts import redirect, render
from django.contrib import messages
from .cart import Cart
# Create your views here.

from . forms import CheckoutForm
from order.utils import checkout


def cart_detail(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = checkout(request, form.cleaned_data['first_name'], form.cleaned_data['last_name'], form.cleaned_data['email'],
                             form.cleaned_data['address'], form.cleaned_data['city'], form.cleaned_data['town'], form.cleaned_data['phone'], cart.get_total_cost())
            cart.clear()
            return redirect('success')
    else:
        form = CheckoutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart')

    return render(request, 'cart/cart.html', {'form': form})


def success(request):
    return render(request, 'cart/success.html')
