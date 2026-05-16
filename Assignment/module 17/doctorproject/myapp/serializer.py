from rest_framework import serializers
from .models import *

class DocSerial(serializers.ModelSerializer):
    class Meta:
        model=docinfo
        fields='__all__'

