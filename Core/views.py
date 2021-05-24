from django.shortcuts import render, redirect
from .models import Land, Contact, OtherProperty, Ranch
from django.http import HttpResponse
from LandAdvert.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import threading
# Create your views here.
import threading
from threading import Thread

class EmailThread(threading.Thread):
    def __init__(self, subject, message, recepient):
        self.subject = subject
        self.message = message
        self.EMAIL_HOST_USER = EMAIL_HOST_USER
        self.recepient = recepient
        threading.Thread.__init__(self)

    def run (self):
       send_mail(self.subject, self.message, self.EMAIL_HOST_USER, self.recepient) 







def viewLands(request, id=0):
    if request.method == "GET":
        if id == 0:
            lands = Land.objects.filter(available=True).order_by("-date_created")
            
            context = {
                'lands': lands,
            }
            return render(request, 'lands.html', context=context)
        else:
            try:
                land = Land.objects.get(id=id)
            except Land.DoesNotExist:
                return render(request, '404.html')
                
            context = {
                'land': land,
            }
            return render(request, 'land.html', context=context)
    else:
        return "INVALID METHOD"

def viewOther(request, id=0):
    if request.method == "GET":
        if id == 0:
            otherproperties = OtherProperty.objects.filter(available=True).order_by("-date_created")
            
            context = {
                'otherproperties': otherproperties,
            }
            return render(request, 'otherproperty.html', context=context)
        else:
            try:
                otherproperty = OtherProperty.objects.get(id=id)
            except OtherProperty.DoesNotExist:
                return render(request, '404.html')
            
            context = {
                'property': otherproperty,
            }
            return render(request, 'property.html', context=context)
    else:
        return "INVALID METHOD"

def viewRanches(request, id=0):
    if request.method == "GET":
        if id == 0:
            ranches = Ranch.objects.filter(available=True).order_by("-date_created")
            
            context = {
                'ranches': ranches,
            }
            return render(request, 'ranches.html', context=context)
        else:
            try:
                ranch = Ranch.objects.get(id=id)
            except Ranch.DoesNotExist:
                return render(request, '404.html')
            
            context = {
                'ranch': ranch,
            }
            return render(request, 'ranch.html', context=context)
    else:
        return "INVALID METHOD"

def contactview(request):
    if request.method == "GET":
        context = {
                'message': 'not sent',
            }
        return render(request, 'contact.html', context=context)
    else:
        name = request.POST["name"]
        email = request.POST["email"]
        text = request.POST["text"]
        
        if name and email and text:
            Contact.objects.create(name=name, email=email, message=text)
            
            subject = "message from " + str(email)
            message = text
            recepient = ["besaneservices@gmail.com"]
            context = {
                'message': 'success',
            }
            
            
            emailObj =  EmailThread(subject=subject, message=message, recepient=recepient)
            emailObj.start()
            
            subject = "Dear " + str(name)
            message = "Welcome to besane property services. We will get back to you within 24 Hours"
            recepient = [str(email)]
            
            emailObj2 =  EmailThread(subject=subject, message=message, recepient=recepient)
            emailObj2.start()
            
            
            return render(request, 'contact.html', context=context)
        else:
            context = {
                'message': 'fail',
            }
            return render(request, 'contact.html', context=context)
        
        
