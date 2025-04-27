from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, Message, Comment
from django.views import generic
from django.urls import reverse
from django.db.models import F

# Create your views here.

from django.urls import path

from . import views


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "blog_list"

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-pub_date')

def about(request):
    return render(request, "blog/about.html")

class BlogsView(generic.ListView):
    template_name = "blog/blogs.html"
    context_object_name = "blog_list"

    def get_queryset(self):
        return BlogPost.objects.all().order_by('-pub_date')

def contact(request):
    return render(request, "blog/contact.html")

def submit(request):
    newmessage = Message(name = request.POST["name"], email = request.POST["email"], phone = request.POST["phoneNumber"], body = request.POST["message"])
    newmessage.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("index"))

def single(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk = blogpost_id)
    return render(request, "blog/single.html", {"blogpost": blogpost})

def upvote(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blogpost.rating.upvote = F("upvote") + 1
    blogpost.rating.save()
    blogpost.rating.refresh_from_db()
    return HttpResponseRedirect(reverse("single", args=(blogpost_id,)))

def downvote(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blogpost.rating.downvote = F("downvote") + 1
    blogpost.rating.save()
    blogpost.rating.refresh_from_db()
    return HttpResponseRedirect(reverse("single", args=(blogpost_id,)))

def comment(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    newcomment = Comment(post = blogpost, name = request.POST["name"], body = request.POST["comment"])
    newcomment.save()
    return HttpResponseRedirect(reverse("single", args=(blogpost_id,)))