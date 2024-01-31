from django.db import models


class EntranceExam(models.Model):
    name = models.CharField(max_length=255)
    full_mark = models.IntegerField(default=100)
    pass_mark = models.IntegerField()

    def __str__(self):
        return self.name

class College(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    eligibility_exam = models.ForeignKey(
        EntranceExam, on_delete=models.CASCADE
    )
    offering_college = models.ManyToManyField(
        College
    )

    def __str__(self):
        return self.name



