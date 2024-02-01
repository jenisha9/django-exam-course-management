from django.db import models

LEVEL_CHOICES = [
        ('diploma', 'Diploma Level'),
        ('bachelor', 'Bachelor\'s Level'),
        ('master', 'Master\'s Level'),
    ]

class EntranceExam(models.Model):
    name = models.CharField(max_length=255)
    full_mark = models.IntegerField(default=100)
    pass_mark = models.IntegerField()
    slug = models.SlugField(null=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    description = models.TextField(max_length=1000)
    university = models.CharField(max_length = 200)
    
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



