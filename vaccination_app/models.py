from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Hospital(models.Model):
    name=models.CharField(max_length=150, null=True, blank=True)
    place=models.CharField(max_length=150)
    phone_no=models.IntegerField()
    email=models.EmailField()
    image=models.FileField(upload_to='uploads/')


    def __str__(self):
        return self.name

class Hospital_user(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    gender = models.CharField(max_length=50, null=True)
    phone_no = models.IntegerField(null=True, blank=True)
    hospital = models.ForeignKey(Hospital,on_delete=models.DO_NOTHING,null=True, blank=True)



class Vaccine(models.Model):
    name=models.CharField(max_length=150)
    date=models.DateField()
    description=models.TextField()

    def __str__(self):
        return self.name



class Complaint(models.Model):
    user=models.ForeignKey(Hospital_user,on_delete=models.DO_NOTHING)
    subject=models.CharField(max_length=200)
    complaint=models.TextField()
    date=models.DateField()
    reply=models.TextField(null=True,blank=True)


class Schedule(models.Model):
    hospital=models.ForeignKey(Hospital,on_delete=models.DO_NOTHING,null=True,blank=True)
    vaccine=models.ForeignKey(Vaccine,on_delete=models.DO_NOTHING,null=True,blank=True)
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()


class Book_appointment(models.Model):
    user=models.ForeignKey(Hospital_user,on_delete=models.CASCADE)
    schedule=models.ForeignKey(Schedule,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)
    vaccine=models.CharField(max_length=250,blank=True,null=True)


