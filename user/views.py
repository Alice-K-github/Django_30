from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from user.Forms import CustomUserCreationForm
from user.models import Pays
from user.serializers import PaysSerializer


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('')


class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('')


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')


class PaysListAPIView(generics.ListAPIView):
    serializer_class = PaysSerializer
    queryset = Pays.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['pay_data']
    search_fields = ['payed_kurs', 'payed_lesson', 'way_to_pay']


