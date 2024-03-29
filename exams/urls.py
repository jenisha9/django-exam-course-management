from django.urls import path

from .views import courses, entrance_exam, exam_detail, result_view

urlpatterns = [
    path("resultview/", result_view, name="resultview"),
    path("resultview/entranceexam/", entrance_exam, name="entrance_exams"),
    path("resultview/courses", courses, name="courses"),
    path("<slug:value>/", exam_detail, name="details"),
]
