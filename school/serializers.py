from rest_framework import serializers
from school.models import Kurs, Lesson



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'name', 'description', 'preview', 'video', 'kurs'
        )

class KursSerializer(serializers.ModelSerializer):
    Lesson_count = serializers.SerializerMethodField()
    Lessons = LessonSerializer(many=True, read_only=True)

    def get_Lesson_count(self, obj):
        return obj.Lesson.count()

    class Meta:
        model = Kurs
        fields = (
            'name', 'description', 'preview'
        )


