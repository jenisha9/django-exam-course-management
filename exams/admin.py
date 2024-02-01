
from django.contrib import admin

from .models import College, Course, EntranceExam

admin.site.register(EntranceExam)
admin.site.register(Course)
admin.site.register(College)

class EntranceExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['exam_name', 'university','exam_date','slug']}),
    ]
    prepopulated_fields = {
        "slug": ("exam_name",),
    }