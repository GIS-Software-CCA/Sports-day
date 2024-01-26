from django.shortcuts import render
from .models import Student,House,Event


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





def signup(request):
    student = Student.objects.get(pk=student_pk)
    return render(request, "student_details.html", {'student': student})
"""
def index(request):
    return render(request, "main.html", {})
"""
