# Generated by Django 4.1.7 on 2023-03-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("emp_app", "0003_rename_phones_employee_phone"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="department",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="role",
        ),
        migrations.DeleteModel(
            name="Department",
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.DeleteModel(
            name="Role",
        ),
    ]
