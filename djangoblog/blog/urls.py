from django.urls import path

from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.BlogsView.as_view(), name="blogs"),
    path("contact/", views.contact, name="contact"),
    path("contact/submit/", views.submit, name="submit"),
    path("blogs/<int:blogpost_id>/", views.single, name="single"),
    path("blogs/<int:blogpost_id>/upvote/", views.upvote, name="upvote"),
    path("blogs/<int:blogpost_id>/downvote/", views.downvote, name="downvote"),
    path("blogs/<int:blogpost_id>/comment/", views.comment, name="comment"),
    #path("blog/", views.blog, name="blog"),
]