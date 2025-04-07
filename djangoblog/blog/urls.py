from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.blogs, name="blogs"),
    path("contact/", views.contact, name="contact"),
    path("blogs/<int:blogpost_id>/", views.single, name="single"),
    #path("blog/", views.blog, name="blog"),
]