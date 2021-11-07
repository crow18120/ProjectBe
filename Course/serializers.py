from rest_framework import serializers
from .models import Course, CourseMaterial


class CourseMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = '__all__'

class CourseSerializers(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
    
    def get_materials(self, obj):
        materials = CourseMaterial.objects.filter(course__id=str(obj.id))
        serializer = CourseMaterialSerializers(materials, many=True)
        return serializer.data