from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .forms import CustomRegForm,NurseRegForm, HospitalForm,VaccineForm
from .models import Hospital,Vaccine,Hospital_user,Complaint,Book_appointment
from .filters import HospitalFilter


def admin_log(request):
    return render(request,'admintemp/dashindex.html')

def create(request):
    form= HospitalForm()
    if request.method=='POST':
        form= HospitalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('view')
    return render(request,'admintemp/hos_create.html',{'form':form})


def view(request):
    form=Hospital.objects.all()
    hospitalFilter=HospitalFilter(request.GET,queryset=form)
    form=hospitalFilter.qs
    context={
        'hospital':form,
        'HospitalFilter':hospitalFilter
    }
    return render(request,'admintemp/hos_view.html',context)


def hos_update(request,id):
    productupdate=Hospital.objects.get(id=id)
    if request.method=='POST':
        updateForm=HospitalForm(request.POST,request.FILES,instance=productupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('view')
    else:
        updateForm=HospitalForm(instance=productupdate)
        return render(request,'admintemp/hos_update.html',{'updateform':updateForm})


def hos_delete(request,dl):
    productdelete=Hospital.objects.get(id=dl)
    productdelete.delete()
    return redirect('view')

def view1(request):
    form = Vaccine.objects.all()
    return render(request, 'admintemp/vacc_view.html', {'form': form})


def vacc_update(request,id):
    productupdate=Vaccine.objects.get(id=id)
    if request.method=='POST':
        updateForm=VaccineForm(request.POST,instance=productupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('view1')
    else:
        updateForm=VaccineForm(instance=productupdate)
    return render(request,'admintemp/vacc_update.html',{'updateform':updateForm})


def vacc_delete(request,dl):
    productdelete = Vaccine.objects.get(id=dl)
    productdelete.delete()
    return redirect('view1')


def cust_view(request):
    form = Hospital_user.objects.filter(is_customer=True)
    return render(request,'admintemp/custmer_view.html', {'form': form})


def cust_update(request,id):
    productupdate = Hospital_user.objects.get(id=id)
    if request.method == 'POST':
        updateForm = CustomRegForm(request.POST, instance=productupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('view1')
    else:
        updateForm = CustomRegForm(instance=productupdate)
    return render(request, 'admintemp/cust_update.html', {'updateform': updateForm})



def cust_delete(request,dl):
    productdelete = Hospital_user.objects.get(id=dl)
    productdelete.delete()
    return redirect('view1')


def nur_view(request):
    form = Hospital_user.objects.filter(is_nurse=True)
    return render(request, 'admintemp/nurse_view.html', {'form': form})


def nur_update(request,id):
    productupdate = Hospital_user.objects.get(id=id)
    if request.method == 'POST':
        updateForm = CustomRegForm(request.POST, instance=productupdate)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('view1')
    else:
        updateForm = CustomRegForm(instance=productupdate)
    return render(request, 'admintemp/nurse_update.html', {'updateform': updateForm})


def nur_delete(request,dl):
    productdelete = Hospital_user.objects.get(id=dl)
    productdelete.delete()
    return redirect('nur_view')

def create1(request):
    form = VaccineForm()
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('view1')
    return render(request, 'admintemp/vacc_create.html', {'form': form})


def reply(request):
    form = Complaint.objects.all()
    print(form)
    return render(request, 'admintemp/reply.html', {'complaint': form})

def admin_reply(request,id):
    complaint=Complaint.objects.get(id=id)
    if request.method=='POST':
        r=request.POST.get('reply')
        print(r)
        complaint.reply=r
        complaint.save()
        return redirect('reply')
    return render(request, 'admintemp/adminreply.html',{'complaint':complaint})

def appointment_view(request):
    form = Book_appointment.objects.all()
    return render(request, 'admintemp/app_view.html', {'form': form})


def approve(request,id):
    n=Book_appointment.objects.get(id=id)
    n.status=1
    n.save()
    messages.info(request,'Appointment confirmed')
    return redirect('appo_view')

def reject(request,id):
    n = Book_appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment rejected')
    return redirect('appo_view')






