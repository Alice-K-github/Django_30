# Generated by Django 5.1.6 on 2025-02-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название')),
                ('description', models.CharField(verbose_name='Описание')),
                ('preview', models.ImageField(upload_to='media/', verbose_name='Изображение(превью)')),
                ('video', models.FileField(upload_to='media/', verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'наименование урока',
                'verbose_name_plural': 'наименования уроков',
            },
        ),
    ]
