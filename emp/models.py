from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(blank=False, primary_key=True)
    employee_code = models.IntegerField()
    name = models.CharField(max_length=45)
    email_id = models.EmailField(blank=True, max_length=45)
    contact_no = models.CharField(max_length=10)

    class Meta:
        db_table = "EmployeeDetails"
