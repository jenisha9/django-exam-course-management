from django.db import models


class EntranceExam(models.Model):
    name = models.CharField(max_length=255)
    full_mark = models.IntegerField(default=100)
    pass_mark = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    eligibility_exam = models.ForeignKey(
        EntranceExam, default=None, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
