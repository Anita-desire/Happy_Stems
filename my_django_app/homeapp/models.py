import email
from email.headerregistry import Address
from django.db import models
from pickle import  TRUE

class users1(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    email=models.EmailField()
    Address=models.CharField(max_length=600)
    PhoneNo=models.CharField(max_length=200)
    

# Create your models here.
