# Generated by Django 5.1.6 on 2025-02-19 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0003_lesson_kurs_alter_kurs_description_alter_kurs_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_data', models.DateTimeField(blank=True, null=True, verbose_name='Дата оплаты')),
                ('pay_sum', models.CharField(blank=True, null=True, verbose_name='Оплаченная сумма')),
                ('way_to_pay', models.CharField(blank=True, choices=[('Перевод', 'Перевод'), ('на', 'На'), ('счёт', 'Счёт')], null=True, verbose_name='Способ оплаты')),
                ('payed_kurs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='School.kurs', verbose_name='Оплаченный курс')),
                ('payed_lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='School.lesson', verbose_name='Оплаченный урок')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'платёж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
