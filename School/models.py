from django.db.models import CASCADE
from rest_framework import serializers
from django.db import models



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


class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = (
            'name', 'description', 'preview'
        )




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
            'name', 'description', 'preview', 'video', 'kurs'
        )

