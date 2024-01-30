from django.shortcuts import get_object_or_404, render

from .models import Course, EntranceExam


def resultview(request):
    entrance_exams = EntranceExam.objects.all()
    courses = Course.objects.all()

    search_exam_id = request.GET.get('search_exam')
    if search_exam_id:
        entrance_exam = get_object_or_404(EntranceExam, pk=search_exam_id)
        courses = Course.objects.filter(eligibility_exam=entrance_exam)

    return render(request, 'exams/resultview.html', {'entrance_exams': entrance_exams, 'courses': courses})