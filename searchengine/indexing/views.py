from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def Import(request):
    return render(request, 'importnew.html')

def Management(request):
        return render(request, '../templates/textmanagement.html')