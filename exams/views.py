from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .models import EntranceExam
from .serializer import EntranceExamSerializer


def exam_list(request):
    if request.method == 'GET':
        exam = EntranceExam.objects.all()
        serializer = EntranceExamSerializer(exam, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EntranceExamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
def exam_detail(request, pk):
    try:
        exam = EntranceExam.objects.get(pk=pk)
    except EntranceExam.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EntranceExamSerializer(exam)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EntranceExamSerializer(exam, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        exam.delete()
        return HttpResponse(status=204)
