from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логин', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Адрес электорнной почты', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Пароль', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Подтверждение пароля', 'class': 'form-control'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логин', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Пароль', 'class': 'form-control'})
