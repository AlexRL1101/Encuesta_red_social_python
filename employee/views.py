from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q
from django.db.models import F, Sum


def employees_list(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees,
    }
    return render(request, 'employee/list.html', context)


def nueva_encuesta(request):
    form = EmployeeForm()

    if request.method == 'POST':
        # form = EmployeeForm(request.POST, request.FILES)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees-message')

    context = {
        'form': form,
    }
    return render(request, 'employee/create.html', context)


def employees_message(request):
    return render(request, 'employee/mensaje.html')


def employees_result(request):
    employees = Employee.objects.all()
    face = Employee.objects.all()

    context = {
        'employees': employees,
        'cantidad': employees.count(),
        'ttfacebook': face,
    }
    return render(request, 'employee/result.html', context)
