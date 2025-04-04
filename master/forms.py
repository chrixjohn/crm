from django.forms import ModelForm
from django import forms
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'dob', 'marital_Status', 'blood_group',
                  'nationality', 'religion', 'category',
                  'permanent_address_1', 'permanent_address_2', 'permanent_city', 'permanent_state', 'permanent_pin',
                  'current_address_1',
                  'current_address_2', 'current_city', 'current_state', 'current_pin',
                  'phone_1', 'phone_2', 'emergency_contact_name1', 'emergency_contact_relation1',
                  'emergency_contact_phone_1', 'emergency_contact_name2', 'emergency_contact_relation2',
                  'emergency_contact_phone_2', 'email',
                  'aadhar_number', 'pan', 'passport_number', 'driving_license_number', 'voter_id',
                  'position_id', 'department_id', 'employment_type', 'join_date', 'date_of_confirmation',
                  'relieve_date', 'office_id', 'reporting_manager',
                  'highest_qualification', 'specialization', 'university', 'year_of_graduation', 'base_salary',
                  'permission_id', 'overtime_id', 'working_hours']

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            'middle_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            'gender': forms.Select(attrs={"class": "form-control"}),
            'dob': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'marital_Status': forms.Select(attrs={"class": "form-control"}),
            'blood_group': forms.Select(attrs={"class": "form-control"}),
            'nationality': forms.TextInput(attrs={"class": "form-control"}),
            'religion': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),

            'permanent_address_1': forms.TextInput(attrs={"class": "form-control"}),
            'permanent_address_2': forms.TextInput(attrs={"class": "form-control"}),
            'permanent_city': forms.TextInput(attrs={"class": "form-control"}),
            'permanent_state': forms.TextInput(attrs={"class": "form-control"}),
            'permanent_pin': forms.TextInput(attrs={"class": "form-control", 'type': 'number'}),
            'current_address_1': forms.TextInput(attrs={"class": "form-control"}),
            'current_address_2': forms.TextInput(attrs={"class": "form-control"}),
            'current_city': forms.TextInput(attrs={"class": "form-control"}),
            'current_state': forms.TextInput(attrs={"class": "form-control"}),
            'current_pin': forms.TextInput(attrs={"class": "form-control", 'type': 'number'}),
            'phone_1': forms.TextInput(attrs={"class": "form-control", 'type': 'number', 'required': 'true'}),
            'phone_2': forms.TextInput(attrs={"class": "form-control", 'type': 'number'}),
            'emergency_contact_name1': forms.TextInput(attrs={"class": "form-control", }),
            'emergency_contact_relation1': forms.TextInput(attrs={"class": "form-control", }),
            'emergency_contact_phone_1': forms.TextInput(attrs={"class": "form-control", 'type': 'number', }),
            'emergency_contact_name2': forms.TextInput(attrs={"class": "form-control", }),
            'emergency_contact_relation2': forms.TextInput(attrs={"class": "form-control", }),
            'emergency_contact_phone_2': forms.TextInput(attrs={"class": "form-control", 'type': 'number', }),
            'email': forms.EmailInput(attrs={"class": "form-control", 'required': 'true'}),

            'aadhar_number': forms.TextInput(attrs={"class": "form-control", 'type': 'number', 'required': 'true'}),
            'pan': forms.TextInput(attrs={"class": "form-control", 'required': 'true'}),
            'passport_number': forms.TextInput(attrs={"class": "form-control"}),
            'driving_license_number': forms.TextInput(attrs={"class": "form-control"}),
            'voter_id': forms.TextInput(attrs={"class": "form-control"}),

            'position_id': forms.Select(attrs={"class": "form-control", 'required': 'true'}),
            'department_id': forms.Select(attrs={"class": "form-control", 'required': 'true'}),
            'employment_type': forms.Select(attrs={"class": "form-control", 'required': 'true'}),
            'join_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date', 'required': 'true'}),
            'date_of_confirmation': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'relieve_date': forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'office_id': forms.Select(attrs={"class": "form-control", 'required': 'true'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
        }

