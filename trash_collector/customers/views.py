from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.urls import reverse
from .models import Customer


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    try:
        customer = Customer.objects.get(user=user)
        return render(request, 'customers/index.html')
    except Customer.DoesNotExist:
        return HttpResponseRedirect(reverse('customers:create'))


def create(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        pickup_day = request.POST.get("pickup_day")
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        new_customer = Customer(name=name, pickup_day=pickup_day, user=user, zip_code=zip_code, address=address)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create_customer.html')


def account_view(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    context = {'customer': customer}
    return render(request, 'customers/account_view.html', context)


def change_pickup(request):
    user = request.user 
    customer = Customer.objects.get(user=user)
    if request.method == "POST":
        new_pickup_day = request.POST.get('pickup_day')
        customer.pickup_day = new_pickup_day
        customer.save()
        return HttpResponseRedirect(reverse('customers:account_view'))    
    else:
        return render(request, 'customers/change_pickup.html')