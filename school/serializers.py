from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from school.models import Kurs, Lesson, Subscription
from school.validators import VideoCustomValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'name', 'description', 'preview', 'video', 'kurs'
        )
        validators = [VideoCustomValidator(field='video')]


class KursSerializer(serializers.ModelSerializer):
    Lesson_count = serializers.SerializerMethodField()
    Is_subscribe = serializers.SerializerMethodField()
    Lessons = LessonSerializer(many=True, read_only=True)

    def get_Lesson_count(self, obj):
        return obj.Lesson.count()

    def is_subscribe(self, obj):
        user = self.request.user
        kurs_id = self.request.data[id]
        kurs_item = get_object_or_404(Kurs, kurs_id)
        subs_item = Subscription.objects.filter(user=user, kurs=kurs_item)
        if subs_item.exists():
            return True
        else:
            return False

    class Meta:
        model = Kurs
        fields = (
            'name', 'description', 'preview',
            'Lessons', 'Lesson_count', 'Is_subscribe'
        )


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'user', 'kurs'
        )
