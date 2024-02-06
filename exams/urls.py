from django.urls import path

from exams import views

urlpatterns = [
    path('exam/', views.ExamList.as_view()),
    path('snippets/<int:pk>/', views.ExamDetail.as_view()),
]