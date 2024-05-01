from django.shortcuts import render
from portfolio.models import portfolio

# Create your views here.
def contact(request):
    return render(request, 'portfolio/contact.html')

def saveEnquiry(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        en=portfolio(name=name, email=email, message=message)
        en.save()
    return render(request, 'portfolio/contact.html')
