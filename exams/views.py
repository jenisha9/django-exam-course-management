from rest_framework import filters, generics

from .models import EntranceExam
from .serializer import EntranceExamSerializer


class ExamList(generics.ListCreateAPIView):
    queryset = EntranceExam.objects.all()
    serializer_class = EntranceExamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'university']
    ordering_fields = ['name', 'full_mark', 'pass_mark']
     
class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntranceExam.objects.all()
    serializer_class = EntranceExamSerializer
    
