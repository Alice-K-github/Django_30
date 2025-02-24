from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from user.views import RegisterView, PaysListAPIView, MyTokenObtainPairView

app_name = 'users'

urlpatterns = [
        path("admin/", admin.site.urls),
        path("logout/", LogoutView.as_view(next_page=''), name="logout"),
        path('login/', LoginView.as_view(), name='login'),
        path('register/', RegisterView.as_view(), name='register'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('pays/list/', PaysListAPIView.as_view(), name='pays_list'),
        path('token/', MyTokenObtainPairView.as_view(),
             name='token_obtain_pair'),
    ]