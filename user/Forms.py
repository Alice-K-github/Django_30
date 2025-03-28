from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import CustomUser


# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text='Введите номер телефона (необязательно).')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError(
                'Номер телефона должен содержать только цифры.'
            )
        return phone_number


# Форма авторизации
class CustomAuthenticationForm(AuthenticationForm):
    pass
