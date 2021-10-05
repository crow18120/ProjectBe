from django.urls import path, include
from . import views

urlpatterns = [
    path('submission/', views.SubmissionList.as_view()),
    # path('submission/<str:pk>/', views.ClassDetail.as_view()),
    # path('material/', views.MaterialList.as_view()),
    # path('material/<str:pk>/', views.MaterialDetail.as_view()),
    # path('materials/<str:pk>/', views.CourseAndMaterials.as_view()),
]
