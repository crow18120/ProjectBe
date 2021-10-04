from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tutor, Staff, Student



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'groups', 'first_name', 'last_name']

class TutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'