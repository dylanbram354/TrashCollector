
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse_lazy
from django.urls import reverse
from django.db.models import Q
from .models import Employee
from datetime import date

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    Customer = apps.get_model('customers.Customer')
    user = request.user
    try:
        employee = Employee.objects.get(user=user)
        zip_code = employee.zip_code
        today_num = date.today().weekday()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        today_day = days[today_num]
        today_date = date.today()
        customers = Customer.objects.filter(Q(zip_code=zip_code),
                                            Q(pickup_day=today_day) | Q(onetime_pickup=today_date),
                                            Q(suspension_start__gte=today_date) | Q(suspension_end__lte=today_date)
                                            | Q(suspension_start=None) | Q(suspension_end=None)
                                            )
        context = {
            'customers': customers
        }
        return render(request, 'employees/index.html', context)
    except Employee.DoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))


def confirm_pickup(request, customer_id):
    user = request.user
    Customer = apps.get_model('customers.Customer')
    customer = Customer.objects.get(id=customer_id)
    if customer.balance is not None:
        customer.balance = customer.balance + 10
    else:
        customer.balance = 10
    customer.save()
    return HttpResponseRedirect(reverse('employees:index'))

   

def create(request):

    user = request.user 
    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=name, zip_code=zip_code, user=user)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create_employee.html')

def filter_pickups(request):

    user = request.user 
    Customer = apps.get_model('customers.Customer')
    if request.method == 'POST':
        employee = Employee.objects.get(user=user)
        zip_code = employee.zip_code
        pickup_day = request.POST.get('Weekday')
        customers = Customer.objects.filter(Q(zip_code=zip_code), Q(pickup_day=pickup_day))

        context = {
            'customers': customers
        }
        return render(request, 'employees/filter_pickup.html', context)
    else:
        return render(request, 'employees/filter_pickup.html')
    

    
