from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid
import pytz

from Course.models import Course
from User.models import Tutor

# Create your models here.
def file_directory_path(instance, filename):
    return "materials/classes/{0}/{1}/{2}".format(
        instance.class_activity.class_obj.name, instance.class_activity.name, filename
    )

def check_submitted_date(value):
    print(timezone.localtime())
    if value  < timezone.now():
        raise ValidationError(
            _('Submitted Date must be in the future.')
        )

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

class ClassActivity(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    class_obj = models.ForeignKey(
        Class, on_delete=models.CASCADE, blank=False, null=False
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    submitted_date = models.DateTimeField(
        null=True, blank=True,
        validators=[check_submitted_date]
    )
    is_assignment = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.name

class ActivityMaterial(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    class_activity = models.ForeignKey(
        ClassActivity, on_delete=models.CASCADE, blank=False, null=False
    )
    file = models.FileField(blank=False, null=False, upload_to=file_directory_path)

    def __str__(self):
        return self.file.name
