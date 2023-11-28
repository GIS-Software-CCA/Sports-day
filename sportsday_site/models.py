from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class House(models.IntegerChoices):
    CHANCELLOR=0,"Chancellor"
    CREST=1,"Crest"
    SULTAN=2,"Sultan"
    QUEEN=3,"Queen"
class Student(models.Model):
    studentid=models.IntegerField(verbose_name="student ID",unique=True)
    firstname=models.CharField(verbose_name="first name",max_length=40)
    lastname=models.CharField(verbose_name="last name",max_length=40)
    yeargroup=models.IntegerField(verbose_name="year group",validators=[MinValueValidator(7),MaxValueValidator(13)],null=True,blank=True)
    tutorgroup=models.CharField(verbose_name="tutor group",max_length=1)
    house=models.IntegerField(choices=House.choices)
    gender=models.CharField(max_length=1,choices=[("M","Male"),("F","Female")])
    def __str__(self):
        return self.firstname+" "+self.lastname
class Event(models.Model):
    name=models.CharField(max_length=40)
    year=models.IntegerField(verbose_name="year held")
    type=models.CharField(max_length=10)#track, field or team
    yeargroup=models.IntegerField(verbose_name="year group",validators=[MinValueValidator(7),MaxValueValidator(13)])
    gender=models.CharField(max_length=1,choices=[("M","Male"),("F","Female")])
    record=models.ForeignKey("Signup",on_delete=models.RESTRICT,blank=True,null=True)
    def __str__(self):
        gen="Boys" if self.gender=="M" else "Girls"
        return f"Year {self.yeargroup} {gen} {self.name} ({self.year})"
class Signup(models.Model):
    signed_student=models.ForeignKey(Student,models.CASCADE,verbose_name="student")
    signed_event=models.ForeignKey(Event,models.CASCADE,verbose_name="event")
    ranking=models.IntegerField(null=True,blank=True)
    result1=models.FloatField(verbose_name="result 1",null=True,blank=True,help_text="Use this for track events")
    result1_fail_type=models.CharField(verbose_name="result 1 fail reason",max_length=20, blank=True, null=True, help_text='Enter the reason why this result is invalid')
    
    result2=models.FloatField(verbose_name="result 2 ",null=True,blank=True)
    result2_fail_type=models.CharField(verbose_name="result 2 fail reason",max_length=20, blank=True, null=True, help_text='Enter the reason why this result is invalid')
    
    result3=models.FloatField(verbose_name="result 3",null=True,blank=True)
    result3_fail_type=models.CharField(verbose_name="result 3 fail reason",max_length=20, blank=True, null=True, help_text='Enter the reason why this result is invalid')
    def printResult(self,resultnum=1):
        if resultnum==1:
            if not self.result1:
                if not self.result1_fail_type:
                    return 'No result recorded'
                else:
                    return self.result1_fail_type

            else:
                return result1
        elif resultnum==2:
            if not self.result2:
                if not self.result2_fail_type:
                    return 'No result recorded'
                else:
                    return self.result2_fail_type

            else:
                return result2
        elif resultnum==3:
            if not self.result3:
                if not self.result3_fail_type:
                    return 'No result recorded'
                else:
                    return self.result3_fail_type

            else:
                return result3
        return "Invalid result number"
