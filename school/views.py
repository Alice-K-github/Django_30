from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

from school.models import Kurs, Lesson
from school.serializers import KursSerializer, LessonSerializer


class Is_Moder(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moders').exists()


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method() in SAFE_METHODS


class Is_Owner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False



class KursViewSet(viewsets.ModelViewSet):
    serializer_class = KursSerializer
    queryset = Kurs.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [Is_Moder, Is_Owner]
        elif self.action == 'list':
            self.permission_classes = [Is_Moder, Is_Owner]
        elif self.action == 'retrieve':
            self.permission_classes = [Is_Moder, Is_Owner]
        elif self.action == 'partial_update':
            self.permission_classes = [Is_Moder, Is_Owner]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            self.permission_classes = [Is_Moder, Is_Owner]
        return [permission() for permission in self.permission_classes]



class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [Is_Moder, Is_Owner]




class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [Is_Moder, Is_Owner]



class LessonCreateAPIViewAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [Is_Moder, Is_Owner]



class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [Is_Owner]



