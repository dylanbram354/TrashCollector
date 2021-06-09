from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.urls import reverse
from .models import Customer
import stripe

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

def add_ontime_pickup(request):
    user = request.user 
    customer = Customer.objects.get(user=user)
    if request.method == "POST":
        ontime_pickup = request.POST.get('ontime_pickup')
        customer.onetime_pickup = ontime_pickup
        customer.save()
        return HttpResponseRedirect(reverse('customers:account_view')) 
    else: 
        return render( request, 'customers/add_extra_pickup.html')

def add_suspension(request):
    user = request.user 
    customer = Customer.objects.get(user=user)
    if request.method == "POST":
        suspension_start = request.POST.get('suspension_start')
        suspension_end = request.POST.get('suspension_end')
        customer.suspension_start = suspension_start
        customer.suspension_end = suspension_end
        customer.save()
        return HttpResponseRedirect(reverse('customers:account_view')) 
    else: 
        return render( request, 'customers/add_suspension.html')

def pay_bill(request):
    user = request.user 
    customer = Customer.objects.get(user=user)

    context = {
        'customer': customer
    }

    return render(request, 'customers/pay_bill.html', context)

def submit_payment(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    if request.method == "POST":
        payment_amount = request.POST.get('payment_amount')
        total_payment =   int(payment_amount) * 100



        stripe.api_key = 'sk_test_51J09k7IegiEVwxhXjGVmOxHgTFqdKvLd18n3vnSTs13X8pv5AOy0QEvKyOGVsfDjiDad3OOIbu1lkm5pf3mfGHHI00shdRRtYE'

        stripe.PaymentIntent.create(
            amount=total_payment,
            currency='usd',
            payment_method_types=['card'],
            receipt_email='jboothwebdev@gmail.com'
        )

        customer.balance -= total_payment / 100
        customer.save()
        return HttpResponseRedirect(reverse('customers:account_view'))
    else:
        context = {
                'customer': customer
            }
        return render(request, 'customers/pay_bill.html', context)
    