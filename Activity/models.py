from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import uuid

from Class.models import Class
from User.models import Student

# Create your models here.
def file_directory_activity_path(instance, filename):
    return "materials/classes/{0}/{1}/{2}".format(
        instance.activity.class_obj.name, instance.activity.name, filename
    )

def file_directory_submission_path(instance, filename):
    return "materials/classes/{0}/{1}/{2}/{3}".format(
        instance.submission.activity.class_obj.name,
        instance.submission.activity.name,
        instance.submission.student.get_fullname(),
        filename
    )

def check_submitted_date(value):
    print(timezone.localtime())
    if value  < timezone.now():
        raise ValidationError(
            _('Submitted Date must be in the future.')
        )

class Activity(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    class_obj = models.ForeignKey(
        Class, on_delete=models.CASCADE, blank=False, null=False
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(
        null=True, blank=True,
        validators=[check_submitted_date]
    )
    is_submit = models.BooleanField(default=False)
    is_assignment = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.name

class ActivityMaterial(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, blank=False, null=False
    )
    file = models.FileField(blank=False, null=False, upload_to=file_directory_activity_path)

    def __str__(self):
        return self.file.name

class Submission(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=False, blank=False
    )
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, null=False, blank=False
    )
    submitted_date = models.DateTimeField(null=True, blank=True)
    graded = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(-1), MaxValueValidator(100)])

    def __str__(self):
        return self.activity.name + "/" + self.student.first_name

class SubmissionMaterial(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    submission = models.ForeignKey(
        Submission, on_delete=models.CASCADE, null=False, blank=False
    )
    file = models.FileField(blank=False, null=False, upload_to=file_directory_submission_path)

