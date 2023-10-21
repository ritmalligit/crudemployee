from django.db import models
from employee.validators import validate_first_name, validate_last_name, validate_employee_id  # Import the new validation function

class Employee(models.Model):
    efirst_name = models.CharField(max_length=20, validators=[validate_first_name], default="")
    elast_name = models.CharField(max_length=20, validators=[validate_last_name], default="")
    eid = models.CharField(max_length=20, validators=[validate_employee_id], unique=True)  # Enforce uniqueness of eid

    eemail = models.EmailField()
    econtact = models.CharField(max_length=10, unique=True)


    def __str__(self):
        return f"{self.efirst_name} {self.elast_name}"

    class Meta:
        db_table = "employee"
