from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,House,Event,Category
import json


# Create your views here

def list_events(request,**kwargs):
    events=Event.objects.filter(**kwargs)
    return render(request, "list_events.html", {"events":events})

def event_details(request,event_pk):
    event=Event.objects.get(pk=event_pk)
    return render(request, "event_details.html", {"event":event})

def student_details(request, student_pk=1):
    student = Student.objects.get(pk=student_pk)
    return render(request, "student_details.html", {'student': student})

def event_selector(request):
    gridl=[]
    options=[{"name":str(i),"url":i.pk} for i in Category.objects.all()]
    return render(request, "event_selector.html", {'options': options,'nextselect':"event_selector_category"})

def event_selector_category(request,category):
    gridl=[]
    options=[{"name":str(i),"url":i.pk} for i in Event.objects.filter(category=category)]
    return render(request, "event_selector.html", {'options': options,'nextselect':"event_details"})

def allstudents(request):
    obj=[]
    for i in Student.objects.all():
        obj.append(i)
    return HttpResponse(json.dumps(obj))

def student_signups(request,houseid,category,gender):
    category_object=Category.objects.get(pk=category)
    house_object=House.objects.get(pk=houseid)
    valid_events=Event.objects.filter(gender=gender,category=category)

    valid_students=Student.objects.filter(gender=gender,category=category)
    gender_string="Boys" if gender=="M" else "Girls" if gender=="F" else "Mixed"
    return render(request, "student_signups.html", {"house":house_object,"category":category_object,"gender":gender_string,"events":valid_events,"students":valid_students})
"""
def index(request):
    return render(request, "main.html", {})
"""
