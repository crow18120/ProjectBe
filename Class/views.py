from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404

from .serializers import (
    ClassSerializers,
    ClassActivitySerializers,
    ActivityMaterialSerializers,
)
from .models import Class, ClassActivity, ActivityMaterial

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


    def get_object(self, pk):
        try:
            return ActivityMaterial.objects.get(pk=pk)
        except ActivityMaterial.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = ActivityMaterialSerializers(material)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = ActivityMaterialSerializers(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        material = self.get_object(pk)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







