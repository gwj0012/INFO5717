from django.shortcuts import render

# Create your views here.

def LoginView(request):
    return render(request, 'login.html')

def NewPassword(request):
    return render(request, 'newpasssword.html')

def Password(request):
    returnrender(request, 'passwordrecovery.html')