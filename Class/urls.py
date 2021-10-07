from django.urls import path, include
from . import views

urlpatterns = [
    path('class/', views.ClassList.as_view()),
    path('class/<str:pk>/', views.ClassDetail.as_view()),
    # path('activity/', views.ActivityList.as_view()),
    # path('activity/<str:pk>/', views.ActivityDetail.as_view()),
    # path('material/', views.MaterialList.as_view()),
    # path('material/<str:pk>/', views.MaterialDetail.as_view()),
    # path('materials/<str:pk>/', views.CourseAndMaterials.as_view()),
]
