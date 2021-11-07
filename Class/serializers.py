from rest_framework import serializers

from Course.models import Course
from Course.serializers import CourseSerializers
from User.models import Tutor
from User.serializers import TutorSerializers
from .models import Class, ClassStudent

class ClassSerializers(serializers.ModelSerializer):
    course_detail = serializers.SerializerMethodField()
    tutor_detail = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = "__all__"

    def get_course_detail(self, obj):
        course_detail = Course.objects.get(id=str(obj.course.id))
        serializer = CourseSerializers(course_detail, many=False)
        return serializer.data
    
    def get_tutor_detail(self, obj):
        tutor_detail = Tutor.objects.get(id=str(obj.tutor.id))
        serializer = TutorSerializers(tutor_detail, many=False)
        return serializer.data

class ClassStudentSerializers(serializers.ModelSerializer):
    class_detail = serializers.SerializerMethodField()

    class Meta:
        model = ClassStudent
        fields = "__all__"
    
    def get_class_detail(self, obj):
        class_detail = Class.objects.get(id=str(obj.class_obj.id))
        serializer = ClassSerializers(class_detail, many=False)
        return serializer.data
