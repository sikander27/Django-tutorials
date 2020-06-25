from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pease.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username','email','password1','password2']
