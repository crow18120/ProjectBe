from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Tutor, Student, Staff

from django.core.mail import send_mail
from django.conf import settings

# def createProfile(sender, instance, created, **kwargs):
#     if created:
#         user = User.objects.get(username = instance.username)
#         print(user.username, ' . ', type(user.username))
#         group = list(user.groups.all())
#         print(group)
        
        


# def updateUser(sender, instance, created, **kwargs):
#     profile = instance
#     user = profile.user

#     if created == False:
#         user.first_name = profile.name
#         user.username = profile.username
#         user.email = profile.email
#         user.save()


# def deleteUser(sender, instance, **kwargs):
#     try:
#         user = instance.user
#         user.delete()
#     except:
#         pass


# post_save.connect(createProfile, sender=User)
# post_save.connect(updateUser, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)
