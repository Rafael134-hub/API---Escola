from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher 
        many = True
        fields = '__all__'