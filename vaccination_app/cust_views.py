from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .forms import CustomRegForm,NurseRegForm, HospitalForm,VaccineForm,ComplaintForm
from .models import Hospital,Vaccine,Hospital_user,Schedule,Complaint,Book_appointment


def cust_log(request):
    return render(request,'custtemp/dashindex1.html')



def complaint_add(request):
    form=ComplaintForm()
    u=request.user
    if request.method=='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect('cmplt_view')
    return render(request,'custtemp/complaint_add.html',{'form':form})



def complaint_view(request):
    form = Complaint.objects.filter(user=request.user)
    return render(request, 'custtemp/complaint_view.html', {'form': form})


def complaint_update(request,id):
    productupdate = Complaint.objects.get(id=id)
    if request.method == 'POST':
        updateForm = ComplaintForm(request.POST,instance=productupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('cmplt_view')
    else:
        updateForm = ComplaintForm(instance=productupdate)
        return render(request, 'custtemp/complaint_update.html', {'updateform': updateForm})


def complaint_delete(request,dl):
    productdelete = Complaint.objects.get(id=dl)
    productdelete.delete()
    return redirect('cmplt_view')


def schedule_view1(request):
    form = Schedule.objects.all()
    return render(request,'custtemp/schedule_view1.html', {'form': form})


def book_appointment(request,id):
    schedule=Schedule.objects.get(id=id)
    data=request.user
    appointment=Book_appointment.objects.filter(user_id=data,schedule=schedule)
    if appointment.exists():
        messages.info(request,'you have already requested appointment for this schedule')
        return redirect('sched_view')
    else:
        if request.method=='POST':
            obj=Book_appointment()
            obj.user=data
            obj.schedule=schedule
            obj.vaccine=schedule.vaccine
            obj.save()
            return redirect('sched_view')
        return render(request,'custtemp/appointment.html',{'schedule':schedule})


def appointment_view1(request):
    form = Book_appointment.objects.filter(user=request.user)
    return render(request, 'custtemp/app_view1.html', {'form': form})

















