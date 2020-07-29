from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=100, required=True)
    password = forms.CharField(label="password", max_length=100, required=True, widget=forms.PasswordInput)
    captcha = CaptchaField()

class NewPass(forms.Form):
    new_password = forms.CharField(label='new_password', max_length=100, required=True, widget=forms.PasswordImput)
    again = forms.CharField(label='again', max_length=100, required=True, widget=forms.PasswordImput)

class Recovery(forms.Form):
    username = forms.CharField(label='username', max_length=100, required=True)
    security = forms.CharField(label='security', max_length=150, required=True)
    answer = forms.CharField(label='answer', max_length=100, required=True)
