from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import Student,House,Signup,Event,Category


# Create your views here

def list_events(request,**kwargs):
    events=Event.objects.filter(**kwargs)
    return render(request, "list_events.html", {"events":events})

def event_details(request,event_pk):
    event=Event.objects.get(pk=event_pk)
    signups=Signup.objects.filter(signed_event=event_pk)
    if request.method=="POST":
        for signup in signups:
            # is each result set for this signup?
            if "result1_"+str(signup.pk) in request.POST:
                result=request.POST["result1_"+str(signup.pk)]
                if result.replace(".","",1).isnumeric():# is it a valid number?
                    signup.result1=float(result)
                    signup.result1_fail_type=""
                else:
                    signup.result1=None
                    signup.result1_fail_type=result
            if "result2_"+str(signup.pk) in request.POST:
                result=request.POST["result2_"+str(signup.pk)]
                if result.replace(".","",1).isnumeric():# is it a valid number?
                    signup.result2=float(result)
                    signup.result2_fail_type=""
                else:
                    signup.result2=None
                    signup.result2_fail_type=result
            if "result3_"+str(signup.pk) in request.POST:
                result=request.POST["result3_"+str(signup.pk)]
                if result.replace(".","",1).isnumeric():# is it a valid number?
                    signup.result3=float(result)
                    signup.result3_fail_type=""
                else:
                    signup.result3=None
                    signup.result3_fail_type=result
            if "ranking_"+str(signup.pk) in request.POST:
                ranking=request.POST["ranking_"+str(signup.pk)]
                if ranking.isnumeric():
                    signup.ranking=int(ranking)
                else:
                    signup.ranking=None
            # Save each signup
            signup.save(update_fields=[
                "result1","result1_fail_type",
                "result2","result2_fail_type",
                "result3","result3_fail_type",
                "ranking"
            ])
        return HttpResponseRedirect(request.path_info)
    return render(request, "event_details.html", {"event":event,"signups":signups.all()})

def event_details_printable(request,event_pk):
    event=Event.objects.get(pk=event_pk)
    signups=Signup.objects.filter(signed_event=event_pk)
    return render(request, "event_printable.html", {"event":event,"signups":signups.all()})


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



def signup(request):
    student = Student.objects.get(pk=student_pk)
    return render(request, "student_details.html", {'student': student})
"""
def index(request):
    return render(request, "main.html", {})
"""
