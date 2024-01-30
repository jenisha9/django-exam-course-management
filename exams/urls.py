from django.urls import path

from .views import resultview

urlpatterns = [
    path('resultview/', resultview, name='resultview'),
    
]