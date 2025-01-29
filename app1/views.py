from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from app1.models import Employee

# Create your views here.

class EmployeeList(ListView):
    model=Employee
    template_name='app1/emplist.html'
    context_object_name='qs'