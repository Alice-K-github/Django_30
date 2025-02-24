from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from school.models import Kurs, Lesson, Subscription
from user.models import CustomUser


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email='admin@example.com', password="123123")
        self.kurs = Kurs.objects.create(name='Курс', description='Описание', owner=self.user)
        self.lesson = Lesson.objects.create(name='Урок', description='Урок1', kurs=self.kurs, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('school:lesson_Retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), self.lesson.name)

    def test_lesson_create(self):
        url = reverse('school:lesson_Create')
        data = {'name': 'Урок2', 'description': 'Урок второй', 'kurs': self.kurs.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('school:lesson_Update', args=(self.lesson.pk,))
        data = {'name': 'Урок3'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'Урок3')

    def test_lesson_delete(self):
        url = reverse('school:lesson_Destroy', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('school:lesson_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {'count': 1, 'next': None, 'previous': None, 'results':
                [{'id': self.lesson.pk, 'name': self.lesson.name, 'description': self.lesson.description,
                  'preview': None, 'video': None,
                  'kurs': self.lesson.kurs.pk, 'owner': self.lesson.owner.pk}]}
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='admin@admin.com', password="123123")
        self.kurs = Kurs.objects.create(name='Джанго', description='Уроки по Джанго', owner=self.user)
        self.lesson = Lesson.objects.create(name='Урок 1', description='Начало', kurs=self.kurs, owner=self.user)
        self.subscription = Subscription.objects.create(kurs=self.kurs, user=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse("school:subscription")
        data = {"kurs": self.kurs.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('message'), 'Подписка отключена')
