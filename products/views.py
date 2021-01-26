from django.shortcuts import render
from .models import Product

# Create your views here.


def all_lessons(request):
    """ A view to show all lesson plans"""

    products = Product.objects.all

    context = {
        'products': products,
    }

    return render(request, "products/products.html", context)
