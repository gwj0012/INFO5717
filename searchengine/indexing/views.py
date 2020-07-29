from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def Import(request):
    return render(request, 'importnew.html')

def Management(request):
    if request.session.get('username') == None:
        return HttpResponseRedirect('/usercontrol/login')
    else:
        return render(request, 'textmanagement.html')