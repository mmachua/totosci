from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils import timezone
from sci import settings
from django.db.models.signals import post_save


class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Business_name = models.CharField(max_length=21, default='')
    county = models.CharField(max_length=100, default='')
    sub_county = models.CharField(max_length=100, default='')
    Estate = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True, default='0')

    def __str__(self):
        return self.user.username


class Client(models.Model):
    
    phone = models.IntegerField(default=0)
    county = models.CharField(max_length=100,blank=True, null=True, default='',choices=(
                                    ('Nairobi', 'Nairobi'),  
                                    ('Nakuru', 'Nakuru')))
    image = models.ImageField(upload_to='profile_image', blank=False ,default='')
    gender = models.CharField(max_length=6,blank=True, null=True, default='',choices=(
                                    ('M', 'Male'),  
                                    ('F', 'Female')))
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

