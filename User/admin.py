from django.contrib import admin
from .models import Tutor, Staff, Student
# Register your models here.
admin.site.register(Tutor)
admin.site.register(Staff)
admin.site.register(Student)