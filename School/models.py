
from django.db.models import CASCADE
from rest_framework import serializers
from django.db import models

from User.models import UserSerializer, CustomUser


class Kurs(models.Model):
    name = models.CharField(
        verbose_name="Название",
        blank=True,
        null=True,
        help_text='Введите название курса'
    )
    preview = models.ImageField(
        upload_to='media/',
        verbose_name='Изображение(превью)',
        blank=True,
        null=True,
        help_text='Укажите превью(изображение)'
    )
    description = models.CharField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text='Введите описание курса'
    )


    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'наименование курса'
        verbose_name_plural = 'наименования курсов'







class Lesson(models.Model):
    name = models.CharField(
        verbose_name="Название",
        blank=True,
        null=True,
        help_text='Введите название урока'
    )

    description = models.CharField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text='Введите описание урока'
        )

    preview = models.ImageField(
        upload_to='media/',
        verbose_name='Изображение(превью)',
        blank=True,
        null=True,
        help_text='Укажите превью(изображение)'
        )

    video = models.URLField(
        verbose_name='Ссылка на видео',
        blank=True,
        null=True,
        help_text='Добавьте ссылку на видео урока'
        )
    kurs = models.ForeignKey(Kurs, on_delete=CASCADE, verbose_name="Курс", blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'наименование урока'
        verbose_name_plural = 'наименования уроков'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id', 'name', 'description', 'preview', 'video', 'kurs'
        )


class KursSerializer(serializers.ModelSerializer):
    Lesson_count = serializers.SerializerMethodField()
    Lessons = LessonSerializer(many=True, read_only=True)

    def get_Lesson_count(self, obj):
        return obj.Lesson.count()

    class Meta:
        model = Kurs
        fields = (
            'id', 'name', 'description', 'preview', 'Lesson_count', 'Lessons'
        )



class Pays(models.Model):
    choices = models.TextChoices('Наличные', 'Перевод на счёт')
    user = models.ForeignKey(CustomUser, on_delete=CASCADE, null=True, blank=True, verbose_name='Пользователь')
    pay_data = models.DateTimeField(verbose_name="Дата оплаты", null=True, blank=True)
    payed_kurs = models.ForeignKey(Kurs, on_delete=CASCADE, verbose_name="Оплаченный курс", null=True, blank=True)
    payed_lesson = models.ForeignKey(Lesson, on_delete=CASCADE, verbose_name="Оплаченный урок", null=True, blank=True)
    pay_sum = models.CharField(verbose_name="Оплаченная сумма", null=True, blank=True)
    way_to_pay = models.CharField(choices=choices, verbose_name='Способ оплаты', null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.payed_kurs} {self.payed_lesson}'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'


class PaysSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    payed_kurs = KursSerializer(read_only=True)
    payed_lesson = LessonSerializer(read_only=True)
    class Meta:
        model = Pays
        fields = (
            'id', 'choices', 'user', 'pay_data', 'payed_kurs', 'payed_lesson', 'pay_sum', 'way_to_pay'
        )


