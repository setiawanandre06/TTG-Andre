from rest_framework import serializers 
from ttgapi_app.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = ('id', 'name', 'email')