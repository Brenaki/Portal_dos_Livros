from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'system/login.html')

def auth(request):
    return render(request, 'system/auth.html')