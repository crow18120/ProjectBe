from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

# Create your models here.
def file_directory_path(instance, filename):
    return "materials/courses/{0}/{1}".format(instance.course.name, filename)


class Course(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    credits = models.IntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CourseMaterial(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=True)
    file = models.FileField(blank=False, null=False, upload_to=file_directory_path)

    def __str__(self):
        return self.file.name