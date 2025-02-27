from celery import shared_task
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from school.models import Subscription, Kurs
from user.models import CustomUser
from django.utils import timezone
from datetime import timedelta


@shared_task
def News_in_kurs(kurs_id):
    kurs = Kurs.objects.get(id=kurs_id)
    users = CustomUser.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(
            kurs=kurs,
            user=user.pk).exists()
        if subscription:
            send_mail(
                subject=f'Обновление курса "{kurs}"',
                message="Обновление материалов курса.",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )


@shared_task
def check_last_login():
    users = CustomUser.objects.filter(last_login__isnull=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} отключен")
        else:
            print(f"Пользователь {user.email} активен")
