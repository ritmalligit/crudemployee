# # validators.py
import re
from django.core.exceptions import ValidationError

def validate_first_name(value):
    if not re.match(r'^[a-zA-Z.]+$', value):
        raise ValidationError('First name cannot contain numbers or special characters except for a dot (.)')
    
def validate_last_name(value):
    if not re.match(r'^[a-zA-Z.]+$', value):
        raise ValidationError('Last name cannot contain numbers or special characters except for a dot (.)')


def validate_employee_id(value):
    if not value.startswith('e'):
        raise ValidationError("Employee ID must start with 'e'.")
    
    try:
        employee_number = int(value[1:])
        if employee_number < 1 or employee_number > 100:
            raise ValidationError("Employee number must be between 1 and 100.")
    except ValueError:
        raise ValidationError("Employee ID must start with 'e' followed by a number.")
    

def validate_contact_number(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("Contact number must be exactly 10 digits.")

def validate_email(value):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
        raise ValidationError("Email address must include '@' symbol and end with '.com'.")