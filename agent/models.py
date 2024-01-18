from django.db import models
from login.models import User

# Create your models here.

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.FileField(upload_to='documents/')

    def __unicode__(self):
        return self.message

