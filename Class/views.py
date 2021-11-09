from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
from django.http import Http404
from Activity.models import Activity, Submission
from Activity.serializers import ActivitySerializers

from User.models import Tutor, Student

from .serializers import (
    ClassSerializers,
    ClassStudentSerializers,
)
from .models import Class, ClassStudent

# Create your views here.

# ClassSerializers
class ClassList(APIView):
    def get(self, request, format=None):
        classes = Class.objects.all()
        serializer = ClassSerializers(classes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassDetail(APIView):
    def get_object(self, pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        class_obj = self.get_object(pk)
        serializer = ClassSerializers(class_obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        class_obj = self.get_object(pk)
        serializer = ClassSerializers(class_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        class_obj = self.get_object(pk)
        class_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ClassStudentSerializers
class ClassStudentList(APIView):
    def get(self, request, format=None):
        classes = ClassStudent.objects.all()
        serializer = ClassStudentSerializers(classes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = ClassStudentSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            activites = Activity.objects.filter(class_obj__id=data.get("class_obj"))
            for item in ActivitySerializers(activites, many=True).data:
                if item["is_submit"]:
                    Submission.objects.create(
                        activity=Activity.objects.get(id=item["id"]),
                        student=Student.objects.get(id=data.get("student")),
                    )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassStudentDetail(APIView):
    def get_object(self, pk):
        try:
            return ClassStudent.objects.get(pk=pk)
        except ClassStudent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        class_obj = self.get_object(pk)
        serializer = ClassStudentSerializers(class_obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        class_obj = self.get_object(pk)
        data = request.data
        print(data)
        serializer = ClassStudentSerializers(class_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            activites = Activity.objects.filter(class_obj__id=data.get("class_obj"))
            for item in ActivitySerializers(activites, many=True).data:
                if item["is_submit"]:
                    Submission.objects.create(
                        activity=Activity.objects.get(id=item["id"]),
                        student=Student.objects.get(id=data.get("student")),
                    )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        class_obj = self.get_object(pk)
        class_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SelectClassWithTutor:
class ClassTutor(APIView):
    def get_object(self, pk):
        try:
            return Tutor.objects.get(pk=pk)
        except Tutor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        self.get_object(pk)
        classes = Class.objects.filter(tutor_id=pk)
        serializer = ClassSerializers(classes, many=True)
        return Response(serializer.data)


class ClassWithStudent(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        self.get_object(pk)
        classes = ClassStudent.objects.filter(student_id=pk)
        serializer = ClassStudentSerializers(classes, many=True)
        return Response(serializer.data)
        
