from django.urls import path
from .views import CreateEmployee, EditEmployee, DeleteEmployee, Home

urlpatterns = [
    path('', Home, name='home'),
    path('create/', CreateEmployee, name='create_new_emp'),
    path('emp_edit/<str:id>/', EditEmployee, name='emp_edit'),
    # path('emp_edit/<str:pk>/', EditEmployee.as_view(), name='emp_edit'),
    path('delete/<str:id>', DeleteEmployee, name='delete'),
]
