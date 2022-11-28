from django.shortcuts import redirect,render
from employee.forms import new_employee , edit_employee
from .models import employee
# Create your views here.

def home(request,a=employee.objects.all()):
    if request.method=='POST':
        fm=new_employee(request.POST)
        if fm.is_valid():
            fm.save()
            fm=new_employee()
            a=employee.objects.all()
    else:
        fm=new_employee()
        a=employee.objects.all()
    return render(request,'home.html',{'forms':fm,'emp_details':a})

def delete(request,id):
    a=employee.objects.get(id=id)
    a.delete()
    return redirect("emp")

def edit(request,id):
    if request.method=="POST":
        print("post se")
        fm=edit_employee(request.POST)
        a=employee.objects.get(id=id)
        print(fm)
        if fm.is_valid():
            new_number=request.POST.get("phone")
            a.phone=new_number
            a.save()
            return redirect("emp")
    else:
        print("get se")
        fm=edit_employee()
        a=employee.objects.get(id=id)
        fm.initial={"phone":a.phone}
    return render(request,"edit.html",{"forms":fm,"a":a})

def filterr(request):
    name=request.GET.get("name")
    if name=="":
        return redirect("emp")
    else:
        obj=employee.objects.filter(first_name__icontains=name)
        fm=new_employee()
        return render(request,'home.html',{'forms':fm,'emp_details':obj})

