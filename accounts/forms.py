from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    fields = ['username', 'password']
    widgets = {
        'username': forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        'password': forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "username")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.fields.get("password"):
            password_help_text = ('<a href="{}">비밀번호변경</a>.').format(f"{reverse('accounts:update_password')}")
            self.fields['password'].help_text = password_help_text