from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Tutor(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profiles/",
        default="user-default.png",
    )
    location = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    DOB = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_fullname(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profiles/",
        default="user-default.png",
    )
    location = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    DOB = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    interest = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_fullname(self):
        return self.first_name + " " + self.last_name


class Staff(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profiles/",
        default="user-default.png",
    )
    location = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    DOB = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_fullname(self):
        return self.first_name + " " + self.last_name
