from django.db import models

# Create your models here.

class doctor(models.Model):
    firstname=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    hospital=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    experience=models.CharField(max_length=20)
    