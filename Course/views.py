from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404

from .models import Course, CourseMaterial
from .serializers import CourseSerializers, CourseMaterialSerializers

# Create your views here.

# CourseSerializers
class CourseList(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        course = Course.objects.all()
        serializer = CourseSerializers(course, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializers(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CourseMaterialSerializers
class CourseMaterialList(APIView):
    def get(self, request, format=None):
        materials = CourseMaterial.objects.all()
        serializer = CourseMaterialSerializers(materials, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CourseMaterialSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        my_file = data.pop("file")
        my_course = data.pop("course")
        for file in my_file:
            CourseMaterial.objects.create(
                file=file, course=Course.objects.get(id=my_course[0])
            )
        return Response(
            CourseSerializers(Course.objects.get(id=my_course[0])).data,
            status=status.HTTP_201_CREATED,
        )


class CourseMaterialDetail(APIView):
    def get_object(self, pk):
        try:
            return CourseMaterial.objects.get(pk=pk)
        except CourseMaterial.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = CourseMaterialSerializers(material)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = CourseMaterialSerializers(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        material = self.get_object(pk)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# FindMaterialsWithCourse


class CourseAndMaterials(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        self.get_object(pk)
        materials = CourseMaterial.objects.filter(course__id=pk)
        serializer = CourseMaterialSerializers(materials, many=True)
        return Response(serializer.data)
