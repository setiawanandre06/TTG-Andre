from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from ttgapi_app.models import Employee
from ttgapi_app.serializers import EmployeeSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def employee_list(request):
    # GET list of employees, POST a new employee, DELETE all employees
    if request.method == 'GET':
        employees = Employee.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            employees = employees.filter(name__icontains=name)
        
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    # find employee by pk (id)
    try: 
        employee = Employee.objects.get(pk=pk) 

        if request.method == 'GET': 
            employee_serializer = EmployeeSerializer(employee) 
            return JsonResponse(employee_serializer.data)
        elif request.method == 'PUT': 
            employee_data = JSONParser().parse(request) 
            employee_serializer = EmployeeSerializer(employee, data=employee_data) 
            if employee_serializer.is_valid(): 
                employee_serializer.save() 
                return JsonResponse(employee_serializer.data) 
            return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            employee.delete() 
            return JsonResponse({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist: 
        return JsonResponse({'message': 'The Employee does not exist'}, status=status.HTTP_404_NOT_FOUND)
