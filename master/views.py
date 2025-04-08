from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from django.utils import timezone
from django.contrib import messages
from .models import Customer
from .forms import *

# Create your views here.

class CustomerList(ListView):
    model = Customer
    template_name = "master/customer_list.html"

    def get(self, request, *args, **kwargs):
        #customer_list = Customer.objects.filter(customer_id=request.user.company_id)
        customer_list= Customer.objects.all()
        context = {'customer_list': customer_list}
        return render(request, self.template_name, context)



def customer_add(request):
    form = CustomerForm()
    context = {'form': form}
    template_name = "master/customer_add.html"
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.create_user = request.user
            data.company_id = request.user.company_id
            data.save()
            messages.success(request, 'Customer Details Added Successfully', 'alert-success')
            return redirect('customer_list')
        else:
            context = {'form': form}
            messages.success(request, 'Invalid Data', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)


def customer_edit(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    form = CustomerForm(instance=customer)
    context = {'form': form, 'customer': customer}
    template_name = "master/customer_edit.html"
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            data = form.save(commit=False)
            data.updated_user = str(request.user)
            data.company_id = request.user.company_id
            data.updated_at = timezone.now()
            data.save()
            messages.success(request, 'Customer Details Updated Successfully', 'alert-success')
            return redirect('customer_list')
        else:
            context = {'form': form, 'customer': customer}
            messages.success(request, 'Invalid Data', 'alert-danger')
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)


class CustomerDetails(TemplateView):
    model = Customer
    template_name = "master/customer_details.html"

    def get(self, request, *args, **kwargs):
        customer_id = self.kwargs.get('pk')
        customer = Customer.objects.get(customer_id=customer_id)
        context = {'customer': customer}
        return render(request, self.template_name, context)