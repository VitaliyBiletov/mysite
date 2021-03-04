from django import forms
from django.contrib.auth.models import User
from .models import Pupil


class UserRegistrationForm(forms.ModelForm):
    # username = forms.CharField(label='Логин', widget=forms.TextInput)
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'groups', 'first_name', 'last_name')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']


class PupilRegistrationForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = ('first_name', 'last_name', 'class_number')