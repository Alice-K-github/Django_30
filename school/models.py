from django.db.models import CASCADE
from django.db import models
from user.models import CustomUser


class Kurs(models.Model):
    # Курсы
    name = models.CharField(verbose_name="Название", blank=True, null=True, help_text='Введите название курса')
    preview = models.ImageField(upload_to='media/', verbose_name='Изображение(превью)',
                                blank=True, null=True, help_text='Укажите превью(изображение)')
    description = models.CharField(verbose_name="Описание", blank=True, null=True, help_text='Введите описание курса')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец карточки', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'наименование курса'
        verbose_name_plural = 'наименования курсов'


class Lesson(models.Model):
    # Уроки
    name = models.CharField(verbose_name="Название", blank=True, null=True, help_text='Введите название урока')
    description = models.CharField(verbose_name="Описание", blank=True, null=True, help_text='Введите описание урока')
    preview = models.ImageField(upload_to='media/', verbose_name='Изображение(превью)',
                                blank=True, null=True, help_text='Укажите превью(изображение)')
    video = models.URLField(verbose_name='Ссылка на видео', blank=True, null=True, help_text='Добавьте ссылку на видео урока')
    kurs = models.ForeignKey(Kurs, on_delete=CASCADE, verbose_name="Курс", blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец карточки', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'наименование урока'
        verbose_name_plural = 'наименования уроков'


class Subscription(models.Model):
    # Подписка
    user = models.ForeignKey(CustomUser, on_delete=CASCADE, verbose_name="Пользователь", blank=True, null=True)
    kurs = models.ForeignKey(Kurs, on_delete=CASCADE, verbose_name="Курс", blank=True, null=True)
