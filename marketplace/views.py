from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'marketplace/index.html')

def pinel(request):
    return render(request, 'marketplace/pinel.html')