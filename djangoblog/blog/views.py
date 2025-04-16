from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import BlogPost
from django.views import generic

# Create your views here.

from django.urls import path

from . import views


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "blog_list"

    def get_queryset(self):
        return BlogPost.objects.all()

def about(request):
    return render(request, "blog/about.html")

class BlogsView(generic.ListView):
    template_name = "blog/blogs.html"
    context_object_name = "blog_list"

    def get_queryset(self):
        return BlogPost.objects.all()

def contact(request):
    return render(request, "blog/contact.html")

def single(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk = blogpost_id)
    return render(request, "blog/single.html", {"blogpost": blogpost})