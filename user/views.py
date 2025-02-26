from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from school.services import create_stripe_price, create_stripe_session
from user.Forms import CustomUserCreationForm
from user.models import Pays
from user.serializers import PaysSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


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

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        price = create_stripe_price(payment.pay_sum)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
