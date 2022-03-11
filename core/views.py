from django.shortcuts import render

# Create your views here.
from product.models import Product


def landing(request):
    newest_products = Product.objects.all()[:8]
    return render(request, 'core/landing.html', {'newest_products': newest_products})


def contact(request):
    return render(request, 'core/contact.html')
