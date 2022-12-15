from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=40)