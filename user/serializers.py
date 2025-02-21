from rest_framework import serializers

import school
from school.serializers import KursSerializer, LessonSerializer
from user.models import CustomUser, Pays


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_staff']


class PaysSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payed_kurs = KursSerializer(read_only=True, many=True)
    payed_lesson = LessonSerializer(read_only=True, many=True)
    class Meta:
        model = Pays
        fields = (
            'id', 'choices', 'user', 'pay_data', 'payed_kurs', 'payed_lesson', 'pay_sum', 'way_to_pay'
        )

