
from django.contrib import admin

from .models import College, Course, EntranceExam

admin.site.register(EntranceExam)
admin.site.register(Course)
admin.site.register(College)

