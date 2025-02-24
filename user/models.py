from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(verbose_name="Аватар", upload_to='pictures/', blank=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=15,
                                    blank=True, help_text='Введите номер телефона (необязательно)')
    country = models.CharField(verbose_name='Страна', max_length=30, blank=True,
                               help_text="Введите страну (необязательно)")
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Pays(models.Model):
    choices = models.TextChoices('Наличные', 'Перевод на счёт')
    user = models.ForeignKey(CustomUser,
                             on_delete=CASCADE,
                             null=True, blank=True,
                             verbose_name='Пользователь')
    pay_data = models.DateTimeField(verbose_name="Дата оплаты",
                                    null=True, blank=True)
    payed_kurs = models.ForeignKey('school.Kurs',
                                   on_delete=CASCADE,
                                   verbose_name="Оплаченный курс",
                                   null=True, blank=True)
    payed_lesson = models.ForeignKey('school.Lesson', on_delete=CASCADE,
                                     verbose_name="Оплаченный урок",
                                     null=True, blank=True)
    pay_sum = models.CharField(verbose_name="Оплаченная сумма",
                               null=True, blank=True)
    way_to_pay = models.CharField(choices=choices,
                                  verbose_name='Способ оплаты',
                                  null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.payed_kurs} {self.payed_lesson}'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'
