from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from School.models import LessonSerializer, Lesson
from School.views import home, KursViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIViewAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = 'School'
router = DefaultRouter()
router.register(r'Kurs', KursViewSet, basename='Kurs')
urlpatterns = router.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', home),
    path('Lessons/', LessonListAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='Lesson_list'),
    path('Lessons/', LessonRetrieveAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='Lesson_Retrieve'),
    path('Lessons/', LessonCreateAPIViewAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='Lesson_Create'),
    path('Lessons/', LessonUpdateAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='Lesson_Update'),
    path('Lessons/', LessonDestroyAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='Lesson_Destroy'),
    ] + router.urls




