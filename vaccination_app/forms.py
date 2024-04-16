import datetime
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

from .models import Hospital_user, Hospital, Vaccine, Complaint, Schedule


class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.TimeInput):
    input_type = 'time'



class CustomRegForm(UserCreationForm):
    class Meta:
        model=Hospital_user
        fields=('first_name','phone_no','gender','username','password1','password2')




class NurseRegForm(UserCreationForm):
    class Meta:
        model=Hospital_user
        fields=('first_name', 'phone_no', 'hospital','username', 'password1', 'password2')




class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields='__all__'


class VaccineForm(forms.ModelForm):
    class Meta:
        model=Vaccine
        fields='__all__'



class ComplaintForm(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model=Complaint
        fields=('date','subject','complaint')


class ScheduleForm(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    start_time=forms.TimeField(widget=TimeInput)
    end_time=forms.TimeField(widget=TimeInput)
    class Meta:
        model=Schedule
        fields=('vaccine','date','start_time','end_time')








