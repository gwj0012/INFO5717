from django import forms

class Recovery(forms.Form):
    username = forms.CharField(label='username', max_length=100, required=True)
    security = forms.CharField(label='security', max_length=150, required=True)
    answer = forms.CharField(label='answer', max_length=100, required=True)