from django.shortcuts import render, HttpResponseRedirect
from .models import TUser, HttpJavascriptResponse
from .userform import UserForm, NewPass, Recovery
import pymysql

# Create your views here.

def LoginView(request):
    userform = UserForm()
    context = {'userform':userform}
    return render(request, '../templates/login.html', context)

def LoginAction(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = TUser.objects.filter(username=username, password=password)
            print(user)
            if len(user) > 0 :
                request.session['username'] = user[0].username
                request.session['password'] = user[0].password
                return HttpResponseRedirect('/indexing/textmanagement')
            else:
                return HttpResponseRedirect('/usercontrol/login')
        else:
            return HttpResponseRedirect('/usercontrol/login')
    else:
        return HttpResponseRedirect('/usercontrol/login')

def NewPassword(request):
    newpass = NewPass()
    context = {'newpass':newpass}
    return render(request, '../templates/newpasssword.html', context)

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
    recovery = Recovery()
    context = {'recovery':recovery}
    return render(request, '../templates/passwordrecovery.html', context)

def Questions(request):
    if request.method == 'POST':
        form = Recovery(request.POST)
        if form.is_valid():
            username = form.POST.get['username']
            security = form.POST.get['security']
            answer = form.POST.get['answer']

            sqlquestion = 'select security_question from TUser where username="str(username)"'
            sqlanswer = 'select security_answer from TUser where username="str(username)"'
            db = pymysql.connect('localhost', 'root', 'python5717', 'pydb')
            cursor = db.cursor()
            sec = cursor.execute(sqlquestion)
            ans = cursor.execute(sqlanswer)
            cursor.close()
            db.close()
            if sec == security and answer == ans:
                return HttpResponseRedirect('/usercontrol/login')
            else:
                HttpResponseRedirect('/usercontrol/newpassword')
        else:
            HttpResponseRedirect('/usercontrol/newpassword')
    else:
        HttpResponseRedirect('usercontrol/newpassword')

def Logout(request):
    del request.session['username']
    del request.session['password']
    return HttpResponseRedirect('/usercontrol/login')
