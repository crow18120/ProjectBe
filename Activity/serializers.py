from rest_framework import serializers
# from .models import ActivityMaterial, Class, ClassActivity
from .models import Activity, ActivityMaterial, Submission, SubmissionMaterial

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"

class ActivityMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityMaterial
        fields = '__all__'

class SubmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class SubmissionMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubmissionMaterial
        fields = '__all__'