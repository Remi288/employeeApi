from django.db import models
from django.db.models import Max

from django.utils import timezone
from datetime import date

# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(
        primary_key=True, editable=False, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    join_date = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-join_date',)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, **kwargs):
        if not self.employee_id:
            max = Employee.objects.aggregate(id_max=Max('employee_id'))[
                'id_max']
            if max is not None:
                maxl = list(max)
                max_int = int(maxl[-1])
                max_int += 1
                max = max_int
            else:
                max = 1
            self.employee_id = "{}{:05d}".format('E',
                            max)  
        super().save(**kwargs) 

