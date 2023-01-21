from django import forms

from .models import Department, Employee

choices = Department.objects.all().values_list('dept', 'dept')

choice_list = []

for item in choices:
    choice_list.append(item)


class CreateEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_id', 'emp_name', 'dept')
        widgets = {

            'emp_id': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dept': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),


        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_name', 'dept')

        widgets = {

            'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dept': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),


        }
