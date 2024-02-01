# Generated by Django 5.0.1 on 2024-01-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_entranceexam_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='entranceexam',
            name='level',
            field=models.CharField(choices=[('diploma', 'Diploma Level'), ('bachelor', "Bachelor's Level"), ('master', "Master's Level")], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
