from .models import EntranceExam
from .serializer import EntranceExamSerializer

from rest_framework import generics


class ExamList(generics.ListCreateAPIView):
    queryset = EntranceExam.objects.all()
    serializer_class = EntranceExamSerializer


class ExamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntranceExam.objects.all()
    serializer_class = EntranceExamSerializer