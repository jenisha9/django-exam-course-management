from django.db import models

LEVEL_CHOICES = [
    ("Diploma", "Diploma Level"),
    ("Bachelors", "Bachelor's Level"),
    ("Masters", "Master's Level"),
]


class EntranceExam(models.Model):
    name = models.CharField(max_length=255)
    full_mark = models.IntegerField(default=100)
    pass_mark = models.IntegerField()
    eligibility_level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    description = models.TextField(max_length=1000)
    university = models.CharField(max_length=200)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    eligibility_exam = models.ForeignKey(EntranceExam, on_delete=models.CASCADE)
    offering_colleges = models.ManyToManyField(College)

    def __str__(self):
        return self.name
