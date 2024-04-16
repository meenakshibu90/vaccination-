from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .forms import CustomRegForm, NurseRegForm, HospitalForm, VaccineForm, ComplaintForm, ScheduleForm
from .models import Hospital,Vaccine,Hospital_user,Complaint,Schedule


def nurse_log(request):
    return render(request,'nursetemp/dashindex2.html')


def nurcomplaint_add(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            return redirect('cmplt_view1')
    return render(request, 'nursetemp/nurcomplaint_add.html', {'form': form})

def nurcomplaint_view(request):
    form = Complaint.objects.filter(user=request.user)
    return render(request, 'nursetemp/nurcomplaint_view.html', {'form': form})


def nurcomplaint_update(request,id):
    productupdate = Complaint.objects.get(id=id)
    if request.method == 'POST':
        updateForm = ComplaintForm(request.POST, instance=productupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('cmplt_view1')
    else:
        updateForm = ComplaintForm(instance=productupdate)
        return render(request, 'nursetemp/nurcomplaint_update.html', {'updateform': updateForm})


def nurcomplaint_delete(request,dl):
    productdelete = Complaint.objects.get(id=dl)
    productdelete.delete()
    return redirect('cmplt_view1')


def schedule(request):
    form=ScheduleForm()
    u=request.user
    r=Hospital_user.objects.filter(username=u).first()
    d=r.hospital
    if request.method=='POST':
        form=ScheduleForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.hospital=d
            obj.save()
            return redirect('sche_view')
    return render(request,'nursetemp/schedule.html',{'form':form})




def schedule_view(request):
    form = Schedule.objects.all()
    return render(request, 'nursetemp/schedule_view.html', {'form': form})

def schedule_update(request,id):
    productupdate = Schedule.objects.get(id=id)
    if request.method == 'POST':
        updateForm = ScheduleForm(request.POST, instance=productupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('sche_view')
    else:
        updateForm = ScheduleForm(instance=productupdate)
        return render(request, 'nursetemp/schedule_update.html', {'updateform': updateForm})

def schedule_delete(request,dl):
    productdelete = Schedule.objects.get(id=dl)
    productdelete.delete()
    return redirect('sche_view')












