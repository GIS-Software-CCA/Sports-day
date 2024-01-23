from django.urls import path
from . import views

urlpatterns = [
    #path('student', views.get_student), # Show a list of all students, wtih link to student details
    path('student/<int:student_pk>', views.student_details,name="student_details"), # Show all a students details
    path('event/<int:event_pk>', views.event_details,name="event_details"),
    path('events', views.list_events,name="list_events_all"),
    path('events/<int:category>', views.list_events,name="list_events_category"),
]
