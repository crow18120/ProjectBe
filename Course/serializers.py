from rest_framework import serializers
from .models import Course, CourseMaterial


class CourseMaterialSerializers(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = CourseMaterial
        fields = "__all__"

    def get_file_name(self, obj):
        file_name = obj.file.name
        return file_name.split("/")[-1]

    def get_file_type(self, obj):
        file_name = self.get_file_name(obj)
        return file_name.split(".")[-1]


class CourseSerializers(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_materials(self, obj):
        materials = CourseMaterial.objects.filter(course__id=str(obj.id))
        serializer = CourseMaterialSerializers(materials, many=True)
        return serializer.data
