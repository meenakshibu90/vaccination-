from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .forms import CustomRegForm,NurseRegForm, HospitalForm,VaccineForm
from .models import Hospital,Vaccine,Hospital_user

# Create your views here.




def cust_reg(request):
    form=CustomRegForm()
    if request.method=='POST':
        form=CustomRegForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_customer=True
            user.save()
            return redirect('index')
    return render(request,'vaccine.html',{'form':form})


def index(request):
    return render(request,'index.html')



def nurse_reg(request):
    form=NurseRegForm()
    if request.method=='POST':
        form=NurseRegForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_nurse=True
            user.save()
            return redirect('index')
    return render(request,'vaccine.html',{'form':form})



def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_log')
            elif user.is_customer:
                return redirect('cust_log')
            elif user.is_nurse:
                return redirect('nurse_log')
    return render(request, 'login.html')


def logout1(request):
    logout(request)
    return redirect('index')
































