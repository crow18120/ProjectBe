from django.urls import path, include
from . import views

urlpatterns = [
    path("class/", views.ClassList.as_view()),
    path("class/<str:pk>/", views.ClassDetail.as_view()),
    path("student/", views.ClassStudentList.as_view()),
    path("student/<str:pk>/", views.ClassStudentDetail.as_view()),
    path("class-tutor/<str:pk>/", views.ClassTutor.as_view()),
    path("class-student/<str:pk>/", views.ClassWithStudent.as_view()),
    path("class-student-with-class/<str:pk>/", views.ClassStudentWithClass.as_view())
]
