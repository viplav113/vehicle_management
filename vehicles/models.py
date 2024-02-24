# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    po_number = models.CharField(max_length=20, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    dc_number = models.CharField(max_length=20)
    po_number = models.CharField(max_length=20)
    
    

from django.db import models

class QualityCheck(models.Model):
    po_number = models.CharField(max_length=50)
    quality_result = models.CharField(max_length=10)  # Assuming it's a CharField, adjust as needed
