from django.shortcuts import render
from settings.models import Employee
# Create your views here.
def nok(request):
    employee = Employee.objects.all()
    return render(request,'index.html',locals())