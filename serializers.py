from rest_framework import serializers
from django.contrib.auth.models import User
from API.models import Employee

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields= "__all__"


   

  