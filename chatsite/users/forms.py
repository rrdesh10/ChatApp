from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')