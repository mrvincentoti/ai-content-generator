from django.shortcuts import render
# from .models import Home, About, Pricing, Feedback, Faqs


# Local import
from dashboard.models import *

# Create your views here.


def home(request):
    homes = Home.objects.all()
    # about = About.objects.all()
    pricing = Pricing.objects.all().order_by('id')
    feedback = Feedback.objects.all()
    faqs = Faqs.objects.all()

    context = {
        'homes': homes,
        # 'about': about,
        'pricing': pricing,
        'feedback': feedback,
        'faqs': faqs,
    }
    return render(request, '../templates/ftth/home.html', context=context)


def contact(request):
    context = {}
    return render(request, 'ftth/contact.html', context)
