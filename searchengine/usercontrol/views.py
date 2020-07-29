from django.shortcuts import render
from usercontrol.models import TUser
from usercontrol.userform import UserForm

# Create your views here.

def LoginView(request):
    return render(request, 'login.html')

def NewPassword(request):
    return render(request, 'newpasssword.html')

def Password(request):
    return render(request, 'passwordrecovery.html')
