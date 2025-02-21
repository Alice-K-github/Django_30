from rest_framework import serializers
from school.models import Kurs, Lesson, Pays
from user.serializers import UserSerializer


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


class PaysSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payed_kurs = KursSerializer(read_only=True)
    payed_lesson = LessonSerializer(read_only=True)
    class Meta:
        model = Pays
        fields = (
            'id', 'choices', 'user', 'pay_data', 'payed_kurs', 'payed_lesson', 'pay_sum', 'way_to_pay'
        )

