from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework import permissions


from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeView(GenericAPIView):
    '''This uses the Django Apiview 
    that allows for reuse of common 
    functionality, and helps us keep our code 
    DRY.

        "get": get all the employees

        "post" Input employee/s details

    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmployeeSerializer
    
    def get(self, request, format=None):
        '''This function get all employees details
        '''
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)


        return Response({"employees": serializer.data })

    
    def post(self, request):
        ''' Create employee details with Post request

        '''
        
        employee_data = request.data
        

        # Above data to create employee data

        with transaction.atomic():
            try:
                first_name = employee_data.get("first_name").title()
                last_name = employee_data.get("last_name").title()
                age = employee_data.get("age")
                data = {**employee_data, "first_name": first_name, "last_name": last_name, "age": age}
                serializer = EmployeeSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    
                else:
                    return Response({"message":"failure to create an employee","error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                status_code = status.HTTP_201_CREATED
                response = {
                    "success": True,
                    "statusCode": status_code,
                    "payload": serializer.data,
                }

                return Response(response, status=status_code)
            except Exception as e:
                return Response({"message":"Failure in creating an employee", "error":str(e)}, status=status.HTTP_400_BAD_REQUEST)









class EmployeeDetailsView(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EmployeeSerializer

    def put(self, request, employee_id):
        ''' Update all or partia; employee details
            "transaction": Help to not automatically save a transaction when part of it fails

        '''

        # update employee using with employee_id

        with transaction.atomic():
            try:
                employee = Employee.objects.get(employee_id=employee_id)
                employee_data = request.data
                first_name = employee_data.get("first_name").title()
                last_name = employee_data.get("last_name").title()
                age = employee_data.get("age")
                data = {**employee_data, "first_name": first_name,
                        "last_name": last_name, "age": age}
                serializer = EmployeeSerializer(
                    instance=employee, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response({"message": "failure to update employee details", "error": serializer.errors},

                                    status=status.HTTP_400_BAD_REQUEST)
                status_code = status.HTTP_200_OK
                response = {
                    "success": True,
                    "statusCode": status_code,
                    "message": "Employee details updated successfully",
                    "payload": serializer.data
                }
                return Response(response, status=status_code)
            except ObjectDoesNotExist:
                return Response({"message": "Employee does not exist"})

    def delete(self, request, employee_id):
        ''' This delete employee details with employee_id

        '''

        try:
            employee = Employee.objects.get(employee_id=employee_id)
            employee.delete()
        except ObjectDoesNotExist:
            return Response({"message": "Employee does not exist"})
        else:
            return Response({"message": "Employee has been deleted successfully."}, status=204)