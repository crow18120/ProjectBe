from rest_framework import serializers
from .models import Course, CourseMaterial

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = '__all__'