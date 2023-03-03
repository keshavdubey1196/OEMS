from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = "role"

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    bonus = models.IntegerField(default=0)
    phones = models.IntegerField(default=0)
    hire_date = models.DateField()

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
