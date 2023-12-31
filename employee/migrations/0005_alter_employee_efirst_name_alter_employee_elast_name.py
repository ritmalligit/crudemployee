# Generated by Django 4.2.2 on 2023-10-20 15:05

from django.db import migrations, models
import employee.validators


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0004_alter_employee_efirst_name_alter_employee_elast_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="efirst_name",
            field=models.CharField(
                default="",
                max_length=20,
                validators=[employee.validators.validate_first_name],
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="elast_name",
            field=models.CharField(
                default="",
                max_length=20,
                validators=[employee.validators.validate_last_name],
            ),
        ),
    ]
