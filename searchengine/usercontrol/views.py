from django.shortcuts import render, HttpResponseRedirect
from usercontrol.models import TUser
from usercontrol.userform import UserForm

# Create your views here.

def LoginView(request):
    userform = UserForm()
    context = {'userform':userform}
    return render(request, 'login.html', context)

def LoginAction(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = TUser.objects.filter(username=username, password=password)
            print(userid)
            if len(user) > 0 :
                request.session['username'] = user[0].username
                request.session['password'] = user[0].password
                return render(request, 'textmanagement.html')
            else:
                return HttpResponseRedirect('/usercontrol/login')
        else:
            return HttpResponseRedirect('/usercontrol/login')
    else:
        return HttpResponseRedirect('/usercontrol/login')

def NewPassword(request):
    return render(request, 'newpasssword.html')

def Password(request):
    return render(request, 'passwordrecovery.html')

def Logout(request):
    del request.session['username']
    del request.session['password']
    return HttpResponseRedirect('/usercontrol/login')