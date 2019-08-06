from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse('Welcome to the Tinyapp\'s Homepage!')
    return render(request, 'home/home.html')

def machineintelligence(request):
    return render(request, 'home/machineintelligence.html')
