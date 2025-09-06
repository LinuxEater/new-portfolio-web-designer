from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def budget(request):
    return render(request, 'budget.html')

def projects(request):
    return render(request, 'projects.html')
