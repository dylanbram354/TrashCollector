from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('account_view/', views.account_view, name='account_view'),
    path('change_pickup/', views.change_pickup, name='change_pickup'),
    path('add_pickup/', views.add_ontime_pickup, name='add_pickup'),
    path('suspension/', views.add_suspension, name='suspension'),
    path('pay_bill', views.pay_bill, name='pay_bill'),
    path('submit_payment', views.submit_payment, name="submit_payment")
]
