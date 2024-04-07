from django.db import models

# Create your models here.

class login(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class signup(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)