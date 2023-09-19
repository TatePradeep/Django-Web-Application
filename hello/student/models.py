from django.db import models

class stud(models.Model):
   date=models.DateField()
   time=models.TimeField()  

class stud2(models.Model):
   name=models.CharField(max_length=100)
   date=models.DateField()
   time=models.TimeField() 
   
        