from django.urls import path
from django.contrib import admin
from .views import CustomerList, customer_add, customer_edit, CustomerDetails

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer_list'),
    path('customers/add/', customer_add, name='customer_add'),
    path('customers/edit/<int:pk>/', customer_edit, name='customer_edit'),
    path('customers/details/<int:pk>/', CustomerDetails.as_view(), name='customer_details'),


]
