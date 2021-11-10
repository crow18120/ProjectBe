from django.urls import path, include
from . import views


urlpatterns = [
    path("account/", views.UserList.as_view(), name="user-list"),
    path("account/<str:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("student/", views.StudentList.as_view(), name="student-list"),
    path("student/<str:pk>/", views.StudentDetail.as_view(), name="student-detail"),
    path("tutor/", views.TutorList.as_view(), name="tutor-list"),
    path("tutor/<str:pk>/", views.TutorDetail.as_view(), name="tutor-detail"),
    path("staff/", views.StaffList.as_view(), name="staff-list"),
    path("staff/<str:pk>/", views.StaffDetail.as_view(), name="staff-detail"),
    path("signout/blacklist/", views.BlacklistTokenView.as_view(), name="blacklist"),
    path("stu-class/<str:pk>/", views.StudentsWithClass.as_view()),
    path("stu-act/<str:pk>/", views.StudentsWithActivity.as_view()),
    path("tutor-class/<str:pk>/", views.TutorWithClass.as_view()),
]
