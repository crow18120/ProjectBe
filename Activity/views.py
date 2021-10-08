from datetime import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404

from User.models import Student

from .serializers import (
    ActivitySerializers,
    ActivityMaterialSerializers,
    SubmissionSerializers,
    SubmissionMaterialSerializers,
)
from Class.serializers import ClassStudentSerializers
from .models import Activity, ActivityMaterial, Submission, SubmissionMaterial
from Class.models import ClassStudent, Class

# Create your views here.

# ActivitySerializers
class ActivityList(APIView):
    def get(self, request, format=None):
        activities = Activity.objects.all()
        serialzer = ActivitySerializers(activities, many=True)
        return Response(serialzer.data)

    def post(self, request, format=None):
        data = request.data
        if data.get('is_assigment'):
            data._mutable = True
            data['is_submit'] = True
            data._mutable = False
        if data.get("is_assignment") and data.get("submitted_date") == None:
            return Response(
                {"error": "Assigment needs define the submitted date."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ActivitySerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        activity = serializer.save()
        if data.get("is_submit"):
            class_student = ClassStudent.objects.filter(class_obj__id = data.get('class_obj'))
            class_student_serializer = ClassStudentSerializers(class_student, many = True)
            for data in class_student_serializer.data:
                Submission.objects.create(student = Student.objects.get(id = data.student), activity = Activity.objects.get(id = activity.id), )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class ActivityDetail(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        activity = self.get_object(pk)
        serializer = ActivitySerializers(activity)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        activity = self.get_object(pk)
        data = request.data
        data._mutable = True
        data["class_obj"] = activity.class_obj.id
        data._mutable = False
        if data.get("is_assignment") and data.get("submitted_date") == None:
            return Response(
                {"error": "Assigment needs define the submitted date."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ActivitySerializers(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ActivityMaterialSerializer
class ActivityMaterialList(APIView):
    def get(self, request, format=None):
        materials = ActivityMaterial.objects.all()
        serializer = ActivityMaterialSerializers(materials, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ActivityMaterialSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        my_file = data.pop("file")
        my_activity = data.pop("activity")
        for file in my_file:
            ActivityMaterial.objects.create(
                file=file, activity=Activity.objects.get(id=my_activity[0])
            )
        return Response(None)

class ActivityMaterialDetail(APIView):
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


# SubmissionSerializers
class SubmissionList(APIView):
    def get(self, request, format=None):
        submissions = Submission.objects.all()
        serialzer = SubmissionSerializers(submissions, many=True)
        return Response(serialzer.data)

class SubmissionDetail(APIView):
    def get_object(self, pk):
        try:
            return Submission.objects.get(pk=pk)
        except Submission.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        submission = self.get_object(pk)
        serializer = SubmissionSerializers(submission)
        return Response(serializer.data)

    # Define Grade submission for Tutor:
    def put(self, request, pk, format=None):
        submission = self.get_object(pk)
        data = request.data
        data._mutable = True
        data["student"] = submission.student.id
        data["activity"] = submission.activity.id
        data["submitted_date"] = submission.submitted_date
        data._mutable = False
        serializer = SubmissionSerializers(submission, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# SubmissionMaterialSerializers
class SubmissionMaterialList(APIView):
    def get(self, request, format=None):
        materials = SubmissionMaterial.objects.all()
        serialzer = SubmissionMaterialSerializers(materials, many=True)
        return Response(serialzer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SubmissionMaterialSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        my_file = data.pop("file")
        my_submission = data.pop("submission")
        submission = Submission.objects.get(id=my_submission[0])
        if submission.activity.deadline_date < timezone.now():
            return Response(
                {"error": "There is too late to submit your files."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        submission.submitted_date = timezone.now()
        submission.save()
        for file in my_file:
            SubmissionMaterial.objects.create(file=file, submission=submission)
        return Response(None)

class SubmissionMaterialDetail(APIView):
    def get_object(self, pk):
        try:
            return SubmissionMaterial.objects.get(pk=pk)
        except SubmissionMaterial.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        material = self.get_object(pk)
        serializer = SubmissionMaterialSerializers(material)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        material = self.get_object(pk)
        data = request.data
        data._mutable = True
        data["submission"] = material.submission.id
        data._mutable = False
        if material.submission.activity.deadline_date < timezone.now():
            return Response(
                {"error": "There is too late to update your files."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        material.submission.submitted_date = timezone.now()
        material.submission.save()
        serializer = ActivityMaterialSerializers(material, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        material = self.get_object(pk)
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ClassAndActivities
class ClassAndActivities(APIView):
    def get_object(self, pk):
        try:
            return Class.objects.get(pk=pk)
        except Class.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        self.get_object(pk)
        activities = Activity.objects.filter(class_obj__id=pk)
        serializer = ActivitySerializers(activities, many=True)
        return Response(serializer.data)


class ActivityAndMaterials(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        self.get_object(pk)
        materials = ActivityMaterial.objects.filter(activity__id=pk)
        serializer = ActivityMaterialSerializers(materials, many=True)
        return Response(serializer.data)

# SubmissionAndMaterial
    