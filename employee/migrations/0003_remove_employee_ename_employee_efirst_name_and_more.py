# Generated by Django 4.2.2 on 2023-10-20 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_auto_20231020_0826"),
    ]

    operations = [
        migrations.RemoveField(model_name="employee", name="ename",),
        migrations.AddField(
            model_name="employee",
            name="efirst_name",
            field=models.CharField(default="efirst_name", max_length=20),
        ),
        migrations.AddField(
            model_name="employee",
            name="elast_name",
            field=models.CharField(default="efirst_name", max_length=20),
        ),
    ]