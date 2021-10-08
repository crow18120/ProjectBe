from django.db import models
import uuid

from Course.models import Course
from User.models import Tutor, Student

# Create your models here.
class Class(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=False, blank=False
    )
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name

class ClassStudent(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, null=False, blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)