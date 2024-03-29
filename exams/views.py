from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Course, EntranceExam


def result_view(request):
    entrance_exams = EntranceExam.objects.all()
    courses = Course.objects.all()

    search_exam_id = request.GET.get("search_exam")
    if search_exam_id:
        courses = Course.objects.filter(
            eligibility_exam=get_object_or_404(EntranceExam, pk=search_exam_id)
        )
    return render(
        request,
        "exams/resultview.html",
        {"entrance_exams": entrance_exams, "courses": courses},
    )


def entrance_exam(request):
    entrance_exams = EntranceExam.objects.all()
    return render(
        request, "exams/entrance_exam.html", {"entrance_exams": entrance_exams}
    )


def courses(request):
    courses = Course.objects.all()
    return render(request, "exams/course.html", {"courses": courses})


def exam_detail(request, value):
    exam_detail = EntranceExam.objects.filter(slug=value)
    if not exam_detail:
        raise Http404
    return render(request, "exams/exam_detail.html", {"exam_detail": exam_detail})
