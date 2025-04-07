from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.

from django.urls import path

from . import views

def index(request):
    return render(request, "blog/index.html")

def about(request):
    return render(request, "blog/about.html")

def blogs(request):
    return render(request, "blog/blogs.html")

def contact(request):
    return render(request, "blog/contact.html")

def single(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk = blogpost_id)
    return render(request, "blog/single.html", {"blogpost": blogpost})