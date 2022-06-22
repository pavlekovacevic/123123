from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class EmployeeManager(BaseUserManager):

    def create_new_employee(self, email, name, password):
        if not email:
            raise ValueError('All new employees must have a valid email adress')

        email = self.normalize_email(email)
        employee = self.model(email=email, name=name)

        employee.set_password(password)
        employee.save(using=self._db)

        return employee

    def create_superuser(self, email, name, password):
        manager = self.create_new_employee(email, name, password)

        manager.is_superuser = True
        manager.is_staff = True
        manager.save(using=self._db)

        return manager
        

class Employee(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)


    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """return string representation of our user """
        return self.email

class Equipment(models.Model):
    device_name = models.CharField(max_length=100)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    

    def get_device_name(self):
        return self.device_name