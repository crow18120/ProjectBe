from rest_framework import serializers

from Course.serializers import CourseSerializers
from .models import Class, ClassStudent

class ClassSerializers(serializers.ModelSerializer):
    course = CourseSerializers(many=False)

    class Meta:
        model = Class
        fields = "__all__"

class ClassStudentSerializers(serializers.ModelSerializer):
    class_obj = ClassSerializers(many=False)

    class Meta:
        model = ClassStudent
        fields = "__all__"
