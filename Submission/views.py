from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SubmissionSerializers, SubmissionMaterialSerializers
from .models import Submission, SubmissionMaterial

# Create your views here.

#StudentActivitySerializers
class SubmissionList(APIView):
    def get(self, request, format=None):
        submissions = Submission.objects.all()
        serializer = SubmissionSerializers(submissions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['grade'] = -1
        print(data)
        serializer = SubmissionSerializers(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        my_file = data.get('file')
        return Response(None)   

# class MaterialDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return ActivityMaterial.objects.get(pk=pk)
#         except ActivityMaterial.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         material = self.get_object(pk)
#         serializer = ActivityMaterialSerializers(material)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         material = self.get_object(pk)
#         serializer = ActivityMaterialSerializers(material, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         material = self.get_object(pk)
#         material.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
