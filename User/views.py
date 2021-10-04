from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Tutor, Student, Staff
from .serializers import (
    UserSerializers,
    TutorSerializers,
    StudentSerializers,
    StaffSerializers,
)

# Create your views here.

# UserSerializers
USER_GROUP = {
    1: "Staff",
    2: "Tutor",
    3: "Student",
}

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=data["username"],
                password=data["password"],
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )
            group = Group.objects.get(id=data["groups"][0])
            user.groups.add(group)

            if USER_GROUP[data["groups"][0]] == 'Staff':
                Staff.objects.create(
                    user=user,
                    username=data["username"],
                    email=data["email"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                )
            elif USER_GROUP[data["groups"][0]] == 'Tutor':
                Tutor.objects.create(
                    user=user,
                    username=data["username"],
                    email=data["email"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                )
            else:
                Student.objects.create(
                    user=user,
                    username=data["username"],
                    email=data["email"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                )
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializers(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        data = request.data
        data['username'] = user.username
        serializer = UserSerializers(user, data=data)
        if serializer.is_valid():
            serializer.save()
            if 'password' in data:
                user.set_password(data['password'])
                user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#StudentSerializers
class StudentList(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data)

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(id=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializers(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        data = request.data
        data['username'] = student.username
        data['email'] = student.email
        data['user'] = student.user.id
        serializer = StudentSerializers(student, data=data)
        if serializer.is_valid():
            serializer.save()
            user = student.user
            user.first_name = student.first_name
            user.last_name = student.last_name
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#TutorSerializers
class TutorList(APIView):
    def get(self, request, format=None):
        tutors = Tutor.objects.all()
        serializer = TutorSerializers(tutors, many=True)
        return Response(serializer.data)

class TutorDetail(APIView):
    def get_object(self, pk):
        try:
            return Tutor.objects.get(id=pk)
        except Tutor.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        tutor = self.get_object(pk)
        serializer = TutorSerializers(tutor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tutor = self.get_object(pk)
        data = request.data
        data['username'] = Tutor.username
        data['email'] = Tutor.email
        data['user'] = Tutor.user.id
        serializer = TutorSerializers(tutor, data=data)
        if serializer.is_valid():
            serializer.save()
            user = tutor.user
            user.first_name = tutor.first_name
            user.last_name = tutor.last_name
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tutor = self.get_object(pk)
        tutor.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#StaffSerializers
class StaffList(APIView):
    def get(self, request, format=None):
        staffs = Staff.objects.all()
        serializer = StaffSerializers(staffs, many=True)
        return Response(serializer.data)

class staffDetail(APIView):
    def get_object(self, pk):
        try:
            return Staff.objects.get(id=pk)
        except Staff.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        staff = self.get_object(pk)
        serializer = StaffSerializers(staff)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        staff = self.get_object(pk)
        data = request.data
        data['username'] = staff.username
        data['email'] = staff.email
        data['user'] = staff.user.id
        serializer = StaffSerializers(staff, data=data)
        if serializer.is_valid():
            serializer.save()
            user = staff.user
            user.first_name = staff.first_name
            user.last_name = staff.last_name
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        staff = self.get_object(pk)
        staff.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#TokenSerializers