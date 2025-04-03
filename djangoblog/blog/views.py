from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.urls import path

from . import views

def index(request):
    return render(request, "blog/index.html")