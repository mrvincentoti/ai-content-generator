from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()


class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()


class Pricing(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    duration = models.IntegerField()
    quantity = models.IntegerField()
    speed = models.CharField(max_length=255)


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    content = models.TextField()


class Faqs(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
