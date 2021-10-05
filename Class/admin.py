from django.contrib import admin
from .models import ClassActivity, Class, ActivityMaterial
# Register your models here.

admin.site.register(Class)
admin.site.register(ClassActivity)
admin.site.register(ActivityMaterial)
