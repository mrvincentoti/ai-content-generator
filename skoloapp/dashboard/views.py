from hashlib import new
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_protect

# Local import
from .forms import *
from .models import *


@login_required
def home(request):
    context = {}
    return render(request, 'dashboard/home.html', context)


def profile(request):
    context = {}

    if request.method == 'GET':
        form = ProfileForm(instance=request.user.profile)
        image_form = ProfileImageForm(instance=request.user.profile)
        context['form'] = form
        context['image_form'] = image_form
        return render(request, 'dashboard/profile.html', context)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        image_form = ProfileImageForm(
            request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
        if image_form.is_valid():
            image_form.save()
            return redirect('profile')

    return render(request, 'dashboard/profile.html', context)


# def addbanner(request):
#     context = {}

#     if request.method == 'GET':
#         return render(request, 'dashboard/add.html', context)

#     if request.method == 'POST':
#         title = request.POST['title']
#         image = request.POST['image']
#         content = request.POST['content']

#         new_home = Home(title=title, image=image, content=content)
#         print(new_home.title, new_home.content, new_home.image)
#         new_home.save()
#         return render(request, 'dashboard/add.html', {})

def addbanner(request):
    if request.method == "POST":
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'dashboard/add.html', {'form': form})

    else:
        form = HomeForm()
    return render(request, 'dashboard/add.html', {'form': form})
