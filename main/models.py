from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255)


class SocialMedia(models.Model):
    instagram = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)


class HomePageDate(models.Model):
    day = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(31)])
    hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
    minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    seconds = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()