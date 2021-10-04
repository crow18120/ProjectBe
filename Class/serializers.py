from rest_framework import serializers
from .models import ActivityMaterial, Class, ClassActivity

class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

class ClassActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassActivity
        fields = "__all__"

class ActivityMaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityMaterial
        fields = '__all__'