# Generated by Django 5.1.6 on 2025-02-19 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название')),
                ('preview', models.ImageField(upload_to='media/', verbose_name='Изображение(превью)')),
                ('description', models.CharField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'наименование курса',
                'verbose_name_plural': 'наименования курсов',
            },
        ),
    ]
