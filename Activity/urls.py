from django.urls import path, include
from . import views


urlpatterns = [
    path("activity/", views.ActivityList.as_view(), name="activity-list"),
    path("activity/<str:pk>/", views.ActivityDetail.as_view(), name="activity-detail"),
    path("ac-material/", views.ActivityMaterialList.as_view(), name="activity-material-list"),
    path("ac-material/<str:pk>/", views.ActivityMaterialDetail.as_view(), name="activity-material-detail"),
    path("submission/", views.SubmissionList.as_view(), name="submission-list"),
    path("submission/<str:pk>/", views.SubmissionDetail.as_view(), name="submission-detail"),
    path("su-material/", views.SubmissionMaterialList.as_view(), name="submission-material-list"),
    path("su-material/<str:pk>/", views.SubmissionMaterialDetail.as_view(), name="submission-material-detail"),
    path("class/<str:pk>/", views.ClassAndActivities.as_view()),
]
