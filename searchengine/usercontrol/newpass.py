from django import forms

class NewPass(forms.Form):
    new_password = forms.CharField(label='new_password', max_length=100, required=True, widget=forms.PasswordInput)
    again = forms.CharField(label='again', max_length=100, required=True, widget=forms.PasswordInput)