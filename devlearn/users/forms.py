from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логин', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Пароль', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Подтверждение пароля', 'class': 'form-control'})

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Логин', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Пароль', 'class': 'form-control'})
