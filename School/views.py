from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from School.models import KursSerializer, Kurs, LessonSerializer, PaysSerializer, Pays


def home(request):
    return render(request, 'home.html')


class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerializer
    queryset = Kurs.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer

class LessonCreateAPIViewAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer

class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer


class PaysListAPIView(generics.ListAPIView):
    serializer_class = PaysSerializer
    queryset = Pays.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['pay_data']
    search_fields = ['payed_kurs', 'payed_lesson', 'way_to_pay']




