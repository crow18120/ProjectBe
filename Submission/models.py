from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

from User.models import Student
# from Class.models import ClassActivity

# Create your models here.
def file_directory_path(instance, filename):
    return "materials/classes/{0}/{1}/{2}/{3}".format(
        instance.student_activity.activity.class_obj.name,
        instance.student_activity.activity.name,
        instance.student_activity.student.get_fullname(),
        filename
    )

class Submission(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=False, blank=False
    )
    activity = models.ForeignKey(
        ClassActivity, on_delete=models.CASCADE, null=False, blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    graded = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(-1), MaxValueValidator(100)])

    def __str__(self):
        return self.activity.name + "/" + self.student.first_name


class SubmissionMaterial(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    student_activity = models.ForeignKey(
        Submission, on_delete=models.CASCADE, null=False, blank=False
    )
    file = models.FileField(blank=False, null=False, upload_to=file_directory_path)
