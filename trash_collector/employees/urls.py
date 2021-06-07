from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('filter/', views.filter_pickups, name='filter'),
    path('confirm_pickup<int:customer_id>/', views.confirm_pickup, name="confirm_pickup")
]