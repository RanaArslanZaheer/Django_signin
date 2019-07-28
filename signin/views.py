from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request, 'signin.html')

def home(request):
    return render(request, 'dashboard/home.html')
