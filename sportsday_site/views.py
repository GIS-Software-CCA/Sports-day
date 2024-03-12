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

def student_signups(request,houseid,category,gender):
    category_object=Category.objects.get(pk=category)
    house_object=House.objects.get(pk=houseid)
    valid_events=Event.objects.filter(gender=gender,category=category)

    valid_students=Student.objects.filter(gender=gender,house=houseid,category=category)
    gender_string="Boys" if gender=="M" else "Girls" if gender=="F" else "Mixed"
    if request.method=="POST":
        valid_input=True
        new_signups={}
        for event in valid_events:
            student_set=set()
            for slotnum in range(2):
                form_field=f"event_{event.pk}_slot_{slotnum+1}"
                if form_field in request.POST:
                    result=request.POST[form_field]
                    if result in student_set:
                        valid_input=False
                        break
                    student_set.add(request.POST[form_field])
            if not valid_input:
                break
            new_signups[event]=student_set
        if valid_input:
            for event in valid_events:
                curev_signups=Signup.objects.filter(signed_event=event,signed_event__gender=gender,signed_student__house=houseid)
                curev_signups.delete()#replace with new signups
                for student_pk in student_set:
                    student_obj=Student.objects.get(pk=student_pk)
                    Signup.objects.create(signed_student=student_obj,signed_event=event)
        else:
            return HttpResponse("error")
        print("form submitted")

        return HttpResponseRedirect(request.path_info)
    return render(request, "student_signups.html", {"house":house_object,"category":category_object,"gender":gender_string,"events":valid_events,"students":valid_students})
"""
def index(request):
    return render(request, "main.html", {})
"""
