from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from school.models import LessonSerializer, Lesson
from school.views import home, KursViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIViewAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView

app_name = 'school'
router = DefaultRouter()
router.register(r'Kurs', KursViewSet, basename='kurs')
urlpatterns = router.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('lessons/', LessonListAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson_Retrieve'),
    path('lessons/new/', LessonCreateAPIViewAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson_Create'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson_Update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer), name='lesson_Destroy'),
    ] + router.urls




