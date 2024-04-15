from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse



def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def services(request):
    return render(request, 'portfolio/services.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')

def contact(request):
    return render(request, 'portfolio/contact.html')



