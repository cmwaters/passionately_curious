from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def library(request):
    return render(request, 'library.html')

def machineintelligence(request):
    return render(request, 'templates/machineintelligence.html')
