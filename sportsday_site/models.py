from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class House(models.Model):
    name=models.CharField(max_length=30)
    colour=models.CharField(max_length=7,help_text="Hex code of the house's colour")#the hex code of the colour
    def __str__(self):
        return self.name
class Category(models.Model): #year group
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="categories"
class Student(models.Model):
    studentid=models.IntegerField(verbose_name="student ID",unique=True)
    firstname=models.CharField(verbose_name="first name",max_length=40)
    lastname=models.CharField(verbose_name="last name",max_length=40)
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.RESTRICT)
    tutorgroup=models.CharField(verbose_name="tutor group",max_length=20)
    house=models.ForeignKey(House,on_delete=models.RESTRICT)
    gender=models.CharField(max_length=1,choices=[("M","Male"),("F","Female")])
    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.tutorgroup})"
class Event(models.Model):
    name=models.CharField(max_length=40)
    year=models.IntegerField(verbose_name="year held")
    type=models.CharField(max_length=10)#track, field or team
    category=models.ForeignKey(Category,on_delete=models.RESTRICT)
    gender=models.CharField(max_length=1,choices=[("M","Male"),("F","Female"),("X","Mixed")])

    # If a school record was created using this platform, this will link to when that occured
    record_signup=models.ForeignKey("Signup",on_delete=models.RESTRICT,blank=True,null=True)
    record_value=models.FloatField(blank=True,null=True)

    #session, group, order
    session_num=models.IntegerField()
    event_group=models.CharField(max_length=20)#two events with same group cannot happen at the same time
    group_order=models.IntegerField()

    def __str__(self):
        gen="Boys" if self.gender=="M" else "Girls" if self.gender=="F" else "Mixed"
        return f"{self.category} {gen} {self.name} ({self.year})"

    def record(self):
        return self.record_signup

    class Meta:
        unique_together=("year","session_num","event_group","group_order")
class Signup(models.Model):
    signed_student=models.ForeignKey(Student,models.CASCADE,verbose_name="student",related_name="signups")
    signed_event=models.ForeignKey(Event,models.CASCADE,verbose_name="event",related_name="signups")
    ranking=models.IntegerField(null=True,blank=True)
    result1=models.FloatField(verbose_name="result 1",null=True,blank=True,help_text="Use this for track events")
    result1_fail_type=models.CharField(verbose_name="result 1 fail reason",max_length=20, blank=True, null=True, help_text='Enter the reason why this result is invalid')

    result2=models.FloatField(verbose_name="result 2",null=True,blank=True)
    result2_fail_type=models.CharField(verbose_name="result 2 fail reason",max_length=20, blank=True, null=True, help_text='Enter the reason why this result is invalid')

    result3=models.FloatField(verbose_name="result 3",null=True,blank=True)
    result3_fail_type=models.CharField(verbose_name="result 3 fail reason",max_length=20, blank=True, null=True, help_text='Enter the reason why this result is invalid')
    def printResult1(self,default=""):
        if self.result1==None:
            if not self.result1_fail_type:
                return default
            else:
                return self.result1_fail_type
        else:
            return self.result1
    def printResult2(self,default=""):
        if self.result2==None:
            if not self.result2_fail_type:
                return default
            else:
                return self.result2_fail_type
        else:
            return self.result2
    def printResult3(self,default=""):
        if self.result3==None:
            if not self.result3_fail_type:
                return default
            else:
                return self.result3_fail_type
        else:
            return self.result3

    class Meta:
        unique_together=("signed_student","signed_event")
