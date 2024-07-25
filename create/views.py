
from django.shortcuts import render, redirect
from .forms import EmployeForm
from .models import Employee 

# Create your views here.

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employe/employee_list.html', context)


def employee_form(request, id=0): # here we working for Edit and delete
    if request.method == "GET":
        if id == 0:
           form = EmployeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeForm(instance=employee)   
        return render(request, 'employe/employe_form.html', {'form':form})
    else:
        if id == 0:
           form = EmployeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeForm(request.POST, instance=employee)   
        if form.is_valid():
          form.save()
        return redirect('/list')    
   


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')        
