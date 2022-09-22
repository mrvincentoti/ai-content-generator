from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('addbanner', views.addbanner, name='addbanner'),
]
