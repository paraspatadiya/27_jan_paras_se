from django.db import models

# Create your models here.



class Course(models.Model):
    course_name=models.CharField(max_length=100)
    course_fees=models.IntegerField()
    course_duration=models.CharField(max_length=100)

class Studinfo(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    address = models.TextField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)




    