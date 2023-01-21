from django import forms
from .models import Student


class CreateStudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class':  'form-control'}))
    present_address = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class':  'form-control'}))
    reg_no = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class':  'form-control'}))

    class Meta:
        model = Student
        fields = ('name', 'present_address', 'reg_no')
