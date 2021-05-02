from django.urls import path, include
from .views import EmployeeView, EmployeeDetailsView

urlpatterns = [
    path('employee/', EmployeeView.as_view(), name="employee"),
    path('employee/<slug:employee_id>', EmployeeDetailsView.as_view()),

]