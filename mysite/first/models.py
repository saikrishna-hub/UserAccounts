from django.db import models
import datetime
from django.utils import timezone
from django.db.models import constraints


# Create your models here.
class  Register(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False,  default="")
    firstname = models.CharField(max_length=100, default="" )
    lastname= models.CharField(max_length=100, default="")
    email= models.EmailField(unique=True, null=False, default="")
    password= models.CharField(max_length=100, null=False, default="")
    hobbies= models.TextField(default="")

    constraints.UniqueConstraint(fields=['username', 'email'], name='unique_details')


    def __str__(self):
        return self.username





