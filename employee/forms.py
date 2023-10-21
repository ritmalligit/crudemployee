from django import forms
from employee.models import Employee
from employee.validators import validate_first_name, validate_last_name, validate_employee_id, validate_contact_number, validate_email

class EmployeeForm(forms.ModelForm):
    efirst_name = forms.CharField(validators=[validate_first_name], max_length=20)
    elast_name = forms.CharField(validators=[validate_last_name], max_length=20)
    eid = forms.CharField(validators=[validate_employee_id], max_length=20)
    econtact = forms.CharField(validators=[validate_contact_number], max_length=10)
    eemail = forms.EmailField(validators=[validate_email])




    class Meta:
        model = Employee
        fields = "__all__"

# from django import forms  
# from employee.models import Employee
# from django.forms import fields

# class EmployeeForm(forms.ModelForm):  
#     class Meta:  
#         model = Employee  
#         fields = "__all__"  