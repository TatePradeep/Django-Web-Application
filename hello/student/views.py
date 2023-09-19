from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from student.models import stud


def student(request):
   if request.method == "POST":
       date=request.POST.get('date')
       time=request.POST.get('time')
       stud1= stud(date=datetime.today,time=time)
       stud1.save()
   return render(request,"student_view.html")

def tutor(request):
    if request.method == "POST":
       name=request.POST.get('name')
       date=request.POST.get('date')
       time=request.POST.get('time')
       stud2= stud(name=name,date=datetime.today,time=time)
       stud2.save()
    return render(request,"tutor_view.html")

def admin1(request):
    return render(request,"admin_view.html")

