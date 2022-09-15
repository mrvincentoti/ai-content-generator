from django.shortcuts import render


# Local import
from .models import *

# Create your views here.


def home(request):
    context = {}
    return render(request, 'ftth/home.html', context)


def contact(request):
    context = {}
    return render(request, 'ftth/contact.html', context)
