from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def index(request):
    all_products = Product.objects.all()
    return render(request, 'basic/products.html', {'products': all_products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'basic/product_details.html', {'product': product})