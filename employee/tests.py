from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class BaseTest(TestCase):
    def setUp(self):
        self.employee_url = reverse('employee')
        self.employee = {
            "first_name": "seun",
            "last_name": "odewale",
            "age": 33
        }
    
        return super().setUp()


class EmployeeTest(BaseTest):

    def test_cannot_create_employee_without_login(self):
        response = self.client.post(
            self.employee_url, self.employee)
        self.assertEqual(response.status_code, 403)

    def test_cant_get_employee_details_without_login(self):
        response = self.client.get(
            self.employee_url, self.employee)
        self.assertEqual(response.status_code, 403)