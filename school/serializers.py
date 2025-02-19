from rest_framework import serializers
from school.models import Kurs, Lesson


class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = (
            'name', 'description', 'preview'
        )


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'name', 'description', 'preview', 'video', 'kurs'
        )

