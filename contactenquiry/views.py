from django.shortcuts import render, redirect
from contactenquiry .models import contactEnquiry


def contact(request):
    return render(request,'portfolio/contact.html')

def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        en = contactEnquiry(name=name, email=email, message=message)
        # Assuming 'contactEnquiry' is your model for storing contact inquiries
        en.save()  # Save the object to the database
    return render(request, 'portfolio/home.html')


    

