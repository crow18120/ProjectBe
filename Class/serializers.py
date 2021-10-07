from rest_framework import serializers
from .models import Class, ClassStudent

class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

class ClassStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = "__all__"
