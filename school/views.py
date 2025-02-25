from rest_framework import viewsets
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (BasePermission,
                                        SAFE_METHODS, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView
from school.paginators import KursPagination, LessonPagination
from school.models import (Kurs, Lesson,
                           Subscription)
from school.serializers import (KursSerializer,
                                LessonSerializer, SubscriptionSerializer)


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
    pagination_class = KursPagination

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

    def get(self, request):
        queryset = Kurs.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = KursSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [Is_Moder, Is_Owner]
    pagination_class = LessonPagination

    def get(self, request):
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


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


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        kurs_id = self.request.data.get(id)
        kurs_item = get_object_or_404(Kurs, kurs_id)
        # объекты подписок по текущему пользователю и курса
        subs_item = Subscription.objects.filter(user=user, kurs=kurs_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            subs_item.create()
            message = 'подписка добавлена'
        return Response({"message": message})
