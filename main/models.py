from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import date
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.OneToOneField(
        User, to_field='username',
        on_delete=models.CASCADE,
        unique=True,primary_key=True,
    )

    country=models.CharField(max_length=100)
    location = models.CharField(max_length=30, blank=True)

    birthdate = models.DateField(null=True, blank=True)
    phone=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='profilepics/%Y/%m/%d/')

    def __str__(self):  # __unicode__ for Python 2
        return self.username.username
