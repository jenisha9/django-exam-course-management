# Generated by Django 5.0.1 on 2024-02-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_entranceexam_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='entranceexam',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='entranceexam',
            name='university',
            field=models.CharField(default='', max_length=200),
        ),
    ]