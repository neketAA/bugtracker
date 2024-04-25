from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Register_Users


class Register_UsersForm(forms.ModelForm):
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже занято. Пожалуйста, выберите другое.")
        return username

    class Meta:
        model = Register_Users
        fields = ['username', 'email', 'password']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя пользователя уже занято. Пожалуйста, выберите другое.")
        return username

    class Meta:
        model = User
        fields = ('username', 'email')
