from rest_framework.serializers import ModelSerializer
from .models import Employee

class EmployeeSerializer(ModelSerializer):

        class Meta:
            model = Employee

            fields = ['employee_id','first_name', 'last_name', 'age',
                  'join_date'
                  ]
