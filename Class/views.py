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


# ClassActivitySerializers
class ActivityList(APIView):
    def get(self, request, format=None):
        activities = ClassActivity.objects.all()
        serialzer = ClassActivitySerializers(activities, many=True)
        return Response(serialzer.data)

    def post(self, request, format=None):
        data = request.data
        if data.get('is_assignment') and data.get('submitted_date') == None:
            return Response({'error': 'Assigment needs define the submitted date.'}, status=status.HTTP_400_BAD_REQUEST)
        serialzer = ClassActivitySerializers(data=data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityDetail(APIView):
    def get_object(self, pk):
        try:
            return ClassActivity.objects.get(pk=pk)
        except ClassActivity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ClassActivitySerializers(activity)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        activity = self.get_object(pk)
        data = request.data
        data._mutable = True
        data['class_obj'] = activity.class_obj.id
        data._mutable = False
        if data.get('is_assignment') and data.get('submitted_date') == None:
            return Response({'error': 'Assigment needs define the submitted date.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ClassActivitySerializers(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#ActivityMaterialSerializers
class MaterialList(APIView):
    def get(self, request, format=None):
        materials = ActivityMaterial.objects.all()
        serializer = ActivityMaterialSerializers(materials, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ActivityMaterialSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        my_file = data.pop('file')
        my_activity = data.pop('class_activity')
        for file in my_file:
            ActivityMaterial.objects.create(file=file, class_activity=ClassActivity.objects.get(id = my_activity[0]))
        return Response(None)   

class MaterialDetail(APIView):
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


#ClassAndActivities
class ClassAndActivities(APIView):
    def get_object(self, pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        self.get_object(pk)
        activities = ClassActivity.objects.filter(class_obj__id=pk)
        serializer = ClassActivitySerializers(activities, many=True)
        return Response(serializer.data)

class ActivityAndMaterials(APIView):
    def get_object(self, pk):
        try:
            return ClassActivity.objects.get(pk=pk)
        except ClassActivity.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        self.get_object(pk)
        materials = ActivityMaterial.objects.filter(class_activity__id=pk)
        serializer = ActivityMaterialSerializers(materials, many=True)
        return Response(serializer.data)
