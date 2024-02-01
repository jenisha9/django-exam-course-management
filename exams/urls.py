from django.urls import path

from exams import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('exam/', views.exam_list),
    path('snippets/<int:pk>/', views.exam_detail),
]