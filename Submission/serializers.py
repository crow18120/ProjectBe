from rest_framework import serializers

from .models import Submission, SubmissionMaterial

class SubmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class SubmissionMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubmissionMaterial
        fields = '__all__'