from rest_framework import serializers

from exams.models import EntranceExam


class EntranceExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceExam
        fields = '__all__'
    