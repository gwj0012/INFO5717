from django.shortcuts import render

# Create your views here.

def Import(request):
    return render(request, 'importnew.html')

def Management(request):
    return render(request, 'textmanagement.html')