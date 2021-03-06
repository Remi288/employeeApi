from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

        class Meta:
            model = Employee

            fields = ['employee_id','first_name', 'last_name', 'age',
                  'join_date'
                  ]
