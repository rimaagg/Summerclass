from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
from blogs.models import Blog, Category

def home(request):
    products = Product.objects.all()
    #blogs = Blog.objects.all()[:3]
    blogs = Blog.objects.all()[:3]

    return render(request, 'extending/home.html',{
        'products': products,
        'blogs': blogs
        })