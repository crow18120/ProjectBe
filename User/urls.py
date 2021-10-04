from django.urls import path, include
from . import views


urlpatterns = [
    path('account/', views.UserList.as_view(), name='user-list'),
    path('account/<str:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('student/', views.StudentList.as_view(), name='student-list'),
    path('student/<str:pk>/', views.StudentDetail.as_view(), name='student-detail'),
]