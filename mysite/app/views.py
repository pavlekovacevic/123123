from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from app.models import Employee, Equipment
from app.serializers import  EquipmentSerializer, EmployeeSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class EmployeeViewSet(viewsets.ModelViewSet):
    """Api that lets employees to be viewed or edited"""
    queryset=Employee.objects.all()
    # authentication_classes=(TokenAuthentication,)
    filter_backends=(filters.SearchFilter)
    serializer_class = EmployeeSerializer
    search_fields = ['name','email']

# class EmployeeLoginApiView(ObtainAuthToken):
#     ...

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    # authentication_classes = (TokenAuthentication,)
    filter_backends=(filters.SearchFilter,)
    serializer_class=EquipmentSerializer
    # permission_classes=[permissions.IsAuthenticated]
    search_fields = ['device_name']

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

