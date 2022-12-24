from django.db import models
from django.contrib.auth.models import User
from turtle import title

# Create your models here.

class patient(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.TextField(max_length=200 , blank=False , null=False)
    age = models.IntegerField()
    Disease = models.TextField(max_length=200 , blank=False , null=False)
    Prescription = models.TextField(max_length=500 , blank=False , null=False)

    def __str__(self):
        return (self.name)

class doctor(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null = True , blank = True)
    name = models.TextField(max_length=200 , blank=False , null=False)
    spec = models.TextField(max_length=200 , null=True , blank=True)
    hosp_name = models.TextField(max_length=200 , blank=False , null=False)
    exp = models.TextField(max_length=200 ,  blank=False , null=False)
    
