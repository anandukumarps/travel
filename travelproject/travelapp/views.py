from django.http import HttpResponse
from django.shortcuts import render
from . models import travel,person
# Create your views here.

def demo(request):
    place=travel.objects.all()
    response=person.objects.all()
    return render(request,'index.html',{'place':place,'person':response})

def about(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    z=x+y
    return render(request,'about.html',{'vn1':z})