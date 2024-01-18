from django.db import models
#from  __future__  import unicode_literals
from login.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Document(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=55, default='')
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    type = models.TextField(max_length=700)
    urgency = models.CharField(max_length=100,blank=True, null=True, default='',choices=(
                                    ('Urgent', 'Urgent'),  
                                    ('Not Urgent', 'Not Urgent')))
    specification = models.CharField(max_length=100,blank=True, null=True, default='',choices=(
                                    ('coloured', 'coloured'),  
                                    ('not coloured', 'not coloured')))
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



    
