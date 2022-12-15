from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def create_employee(request,id=0):
    if(request.method=='GET'):
        if(id==0):
            forms=EmployeeForm
        else:
            rood=Employee.objects.get(pk=id)
            forms=EmployeeForm(insert=rood)
        return render (request,'employee_record/create_employee.html',{"forms":forms})        
    else:
        if(id==0):
            forms =EmployeeForm(request.POST)     
        else:
            rood=Employee.objects.get(pk=id)
            forms=EmployeeForm(request.POST,insert=rood)


        if forms.is_valid():
            forms.save()
        return redirect("/employee/list")

def employee_list(request):
    data={"emp_list":Employee.objects.all()}
    return render(request,'employee_record/employee_list.html',data)


def employee_delete(request,id):
    if (id!=0):
        rood=Employee.objects.get(pk=id)
        rood.delete()
    data={"emp_list":Employee.objects.all()}
    return render(request,'employee_record/employee_list.html',data)
