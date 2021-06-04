from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps

from django.urls import reverse_lazy
from django.urls import reverse
from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')

def create(request):

    user = request.user 
    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=name, zip_code=zip_code, user=user)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index' ))
    else:
        return render(request, 'employees/create_employee.html')
