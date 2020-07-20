from django.shortcuts import render

# Create your views here.

def Display(request):
    return render(request, 'display.html')

def SearchResults(request):
    return render(request, 'searchresults.html')