from django.urls import path, include
from . import views

urlpatterns = [
    path('course/', views.CourseList.as_view()),
    path('course/<str:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('material/', views.CourseMaterialList.as_view()),
    path('material/<str:pk>/', views.CourseMaterialDetail.as_view(), name='materail-detail'),
    path('materials/<str:pk>/', views.CourseAndMaterials.as_view(), name='course-detail-with-material'),
]
