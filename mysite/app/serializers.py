from app.models import Employee, Equipment
from rest_framework import serializers
from app import models

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,    # u can only use it to create new obj, we use extra kwargs to specify more modifications to a certain field
                'style':{'input_type':'password'} # stars when tpying the password
            }
        }

    def create(self, validated_data):
        employee = models.Employee.objects.create_new_employee(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        

        return employee

class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ['id', 'device_name','employee']
        
