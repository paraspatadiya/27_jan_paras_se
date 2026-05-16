from rest_framework import serializers
from .models import *

class StudSerial(serializers.ModelSerializer):
    class Meta:
        model=Studinfo
        fields='__all__'

class CourseSerial(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'