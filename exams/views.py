from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EntranceExam
from .serializer import EntranceExamSerializer


@api_view(["GET", "PUT", "DELETE"])
def exam_detail(request, pk):
    try:
        exam = EntranceExam.objects.get(pk=pk)
    except EntranceExam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = EntranceExamSerializer(exam)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = EntranceExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def exam_list(request):
    if request.method == "GET":
        exam = EntranceExam.objects.all()
        serializer = EntranceExamSerializer(exam, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EntranceExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
