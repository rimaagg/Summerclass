from django.shortcuts import render, get_object_or_404
from . models import Blog, Category

def blog_home(request):
    all_blogs = Blog.objects.all()
    return render(request, 'extending/blogs.html', {'blogs': all_blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'extending/blog_details.html', {'blog': blog})

