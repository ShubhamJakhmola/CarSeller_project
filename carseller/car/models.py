from django.db import models

# Create your models here.
class register(models.Model):
    fname=models.CharField(max_length=20),
    lname=models.CharField(max_length=20),
    email=models.CharField(max_length=20),
    password=models.CharField(max_length=20),
    cpassword=models.CharField(max_length=20),
    
class contactus(models.Model):
    finame=models.CharField(max_length=20),
    lname=models.CharField(max_length=20),
    country=models.CharField(max_length=20),
    subject=models.CharField(max_length=20),
