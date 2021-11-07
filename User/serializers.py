from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tutor, Staff, Student

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http import Http404
import json


def get_tutor(pk):
    try:
        return Tutor.objects.get(user_id=pk)
    except Tutor.DoesNotExist:
        raise Http404


def get_student(pk):
    try:
        return Student.objects.get(user_id=pk)
    except Student.DoesNotExist:
        raise Http404


def get_staff(pk):
    try:
        return Staff.objects.get(user_id=pk)
    except Staff.DoesNotExist:
        raise Http404


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "groups",
            "first_name",
            "last_name",
        ]


class TutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        if len(UserSerializers(user, many=False).data.get("groups")) > 0:
            groups = UserSerializers(user, many=False).data.get("groups")[0]
        else:
            groups = 0
            
        if groups == 1:
            token["account_id"] = str(get_staff(pk=user.id).id)
            token["role"] = "staff"
        elif groups == 2:
            token["account_id"] = str(get_tutor(pk=user.id).id)
            token["role"] = "tutor"
        elif groups == 3:
            token["account_id"] = str(get_student(pk=user.id).id)
            token["role"] = "student"
        else: 
            token["role"] = "admin"

        return token
