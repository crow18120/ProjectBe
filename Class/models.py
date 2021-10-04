from django.db import models
import uuid

from Course.models import Course
from User.models import Tutor
# Create your models here.

class Class(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=False, blank=False)

class ClassActivity(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    submitted_date = models.DateTimeField

