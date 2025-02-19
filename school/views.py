from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from school.models import Kurs, Lesson
from school.serializers import KursSerializer, LessonSerializer


class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerializer
    queryset = Kurs.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonCreateAPIViewAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


