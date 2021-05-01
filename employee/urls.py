from django.urls import path, include
from .views import EmployeeView

urlpatterns = [
    path('employee/', EmployeeView.as_view()),
    path('employee/<slug:employee_id>', EmployeeView.as_view()),

]