from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

# Create your models here.
class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True,blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    create_user = models.ForeignKey('CustomUser', on_delete=models.CASCADE,blank=True, null=True)
    updated_user = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.customer_id}"


class CustomUser(AbstractUser):  # add this in accounts app
    company = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)




    

# class Employee(models.Model):
#     first_name = models.CharField(max_length=100)
#     middle_name = models.CharField(max_length=100, blank=True, null=True)
#     last_name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
#     dob = models.DateField()

#     marital_Status = models.CharField(max_length=20)


#     blood_group = models.CharField(max_length=5)
#     nationality = models.CharField(max_length=50)
#     religion = models.CharField(max_length=50, blank=True, null=True)
#     category = models.CharField(max_length=50, blank=True, null=True)

#     permanent_address_1 = models.CharField(max_length=255)
#     permanent_address_2 = models.CharField(max_length=255, blank=True, null=True)
#     permanent_city = models.CharField(max_length=100)
#     permanent_state = models.CharField(max_length=100)
#     permanent_pin = models.CharField(max_length=10)

#     current_address_1 = models.CharField(max_length=255, blank=True, null=True)
#     current_address_2 = models.CharField(max_length=255, blank=True, null=True)
#     current_city = models.CharField(max_length=100, blank=True, null=True)
#     current_state = models.CharField(max_length=100, blank=True, null=True)
#     current_pin = models.CharField(max_length=10, blank=True, null=True)

#     phone_1 = models.CharField(max_length=15)
#     phone_2 = models.CharField(max_length=15, blank=True, null=True)
#     email = models.EmailField(unique=True)

#     emergency_contact_name1 = models.CharField(max_length=100)
#     emergency_contact_relation1 = models.CharField(max_length=50)
#     emergency_contact_phone_1 = models.CharField(max_length=15)

#     emergency_contact_name2 = models.CharField(max_length=100, blank=True, null=True)
#     emergency_contact_relation2 = models.CharField(max_length=50, blank=True, null=True)
#     emergency_contact_phone_2 = models.CharField(max_length=15, blank=True, null=True)

#     aadhar_number = models.CharField(max_length=20, unique=True)
#     pan = models.CharField(max_length=20, unique=True)
#     passport_number = models.CharField(max_length=20, blank=True, null=True)
#     driving_license_number = models.CharField(max_length=20, blank=True, null=True)
#     voter_id = models.CharField(max_length=20, blank=True, null=True)

#     position_id = models.CharField(max_length=100)
#     department_id = models.CharField(max_length=100)
#     employment_type = models.CharField(max_length=50)
#     join_date = models.DateField()
#     date_of_confirmation = models.DateField(blank=True, null=True)
#     relieve_date = models.DateField(blank=True, null=True)
#     office_id = models.CharField(max_length=100)
#     reporting_manager = models.CharField(max_length=100, blank=True, null=True)

#     highest_qualification = models.CharField(max_length=100, blank=True, null=True)
#     specialization = models.CharField(max_length=100, blank=True, null=True)
#     university = models.CharField(max_length=100, blank=True, null=True)
#     year_of_graduation = models.IntegerField(blank=True, null=True)

#     base_salary = models.DecimalField(max_digits=10, decimal_places=2)
#     permission_id = models.CharField(max_length=100, blank=True, null=True)
#     overtime_id = models.CharField(max_length=100, blank=True, null=True)
#     working_hours = models.IntegerField()


#     class Meta:
#         verbose_name = "Employee"
#         verbose_name_plural = "Employees"
#         ordering = ['dob']
#         indexes = [
#             models.Index(fields=['email']),
#             models.Index(fields=['phone_1']),
#         ]
#         unique_together = ('email', 'phone_1')

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"