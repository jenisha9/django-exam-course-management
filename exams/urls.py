from django.urls import path

from .views import entrance_exam, resultview,courses

urlpatterns = [
    path('resultview/', resultview, name='resultview'),
    path('resultview/entranceexam/', entrance_exam, name='entrance_exams'),
    path('resultview/courses', courses, name='courses')
    
]