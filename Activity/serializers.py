from rest_framework import serializers

from Class.serializers import ClassSerializers
from .models import Activity, ActivityMaterial, Submission, SubmissionMaterial


class ActivityMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityMaterial
        fields = "__all__"


class SubmissionMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubmissionMaterial
        fields = "__all__"


class SubmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"


class ActivitySerializers(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()
    class_obj = ClassSerializers(many=False)

    class Meta:
        model = Activity
        fields = "__all__"

    def get_materials(self, obj):
        materials = ActivityMaterial.objects.filter(activity__id=str(obj.id))
        serializer = ActivityMaterialSerializers(materials, many=True)
        return serializer.data
