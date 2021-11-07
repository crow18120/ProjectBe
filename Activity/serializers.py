from rest_framework import serializers

from Class.serializers import ClassSerializers
from Class.models import Class
from .models import Activity, ActivityMaterial, Submission, SubmissionMaterial


class ActivityMaterialSerializers(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = ActivityMaterial
        fields = "__all__"

    def get_file_name(self, obj):
        file_name = obj.file.name
        return file_name.split("/")[-1]
    
    def get_file_type(self, obj):
        file_name = self.get_file_name(obj)
        return file_name.split(".")[-1]


class SubmissionMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubmissionMaterial
        fields = "__all__"


class SubmissionSerializers(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = "__all__"

    def get_materials(self, obj):
        materials = SubmissionMaterial.objects.filter(submission__id=str(obj.id))
        serializer = SubmissionMaterialSerializers(materials, many=True)
        return serializer.data


class ActivitySerializers(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()
    class_detail = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = "__all__"

    def get_materials(self, obj):
        materials = ActivityMaterial.objects.filter(activity__id=str(obj.id))
        serializer = ActivityMaterialSerializers(materials, many=True)
        return serializer.data

    def get_class_detail(self, obj):
        class_detail = Class.objects.get(id=str(obj.class_obj.id))
        serializer = ClassSerializers(class_detail, many=False)
        return serializer.data
