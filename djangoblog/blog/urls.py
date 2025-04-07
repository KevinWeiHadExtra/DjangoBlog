from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.about, name="about"),
    path("blogs/", views.BlogsView.as_view(), name="blogs"),
    path("contact/", views.contact, name="contact"),
    path("blogs/<int:blogpost_id>/", views.single, name="single"),
    #path("blog/", views.blog, name="blog"),
]