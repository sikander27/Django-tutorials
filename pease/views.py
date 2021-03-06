from django.shortcuts import render, redirect
from pease.forms import EmployeeForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from pease.models import Employee
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def test(request):
    context = {'content':"hello Sikander....!"}
    return render(request, 'base/base.html',context)

@login_required
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                ename = form.cleaned_data.get('ename')
                messages.success(request, f' {ename} has been added!')
                return redirect('/employee/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee/index.html',{'form':form})

def show(request):
    employees = Employee.objects.all()
    return render(request, 'employee/show.html',{'employees':employees})

@login_required
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'employee/edit.html',{'employee':employee})

@login_required
def update(request, id):
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        ename = form.cleaned_data.get('ename')
        messages.success(request, f'Record updated for {ename}')
        return redirect("/employee/show")
    return render(request, 'employee/edit.html',{'employee':employee})

@login_required
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/employee/show")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account for {username}!')
            
            return redirect('login')
            
    else:
        form= UserRegisterForm()
    
    
    return render(request, 'employee/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated profile and user')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'employee/profile.html',context)

