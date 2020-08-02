from django.shortcuts import render, HttpResponseRedirect
from usercontrol.models import TUser, HttpJavascriptResponse
from usercontrol.userform import UserForm, NewPass, Recovery
import pymysql

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
            print(user)
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
    newpass = NewPass()
    context = {'newpass':newpass}
    return render(request, 'newpasssword.html', context)

def NewPassAction(request):
    if request.method == "POST":
        form = NewPass(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            again = form.cleaned_data['again']
            if new_password == again:

                sql = 'update TUser set passowrd="str(new_password)" where iduser="1"'
                print(sql)
                db = pymysql.connect('localhost', 'root', 'python5717', 'pydb')
                cursor = db.cursor()
                cursor.execute(sql)
                db.comit()
                cursor.close()
                db.close()
                return HttpJavascriptResponse("static.inc.javascript.savedpass();")
            else:
                HttpResponseRedirect("/usercontrol/newpassword")
        else:
            HttpResponseRedirect("/usercontrol/newpassword")
    else:
        HttpResponseRedirect("/usercontrol/newpassword")


def Password(request):
    return render(request, 'passwordrecovery.html')

def Logout(request):
    del request.session['username']
    del request.session['password']
    return HttpResponseRedirect('/usercontrol/login')
