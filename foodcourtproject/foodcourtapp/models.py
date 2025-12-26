from django.db import models
from django.utils import timezone
from datetime import timedelta


class Register(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    
    address = models.TextField()

    def __str__(self):
        return self.name


class OTP(models.Model):
    email = models.EmailField()
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=5)

    def __str__(self):
        return f"{self.email} - {self.otp_code}"
from django.db import models

class Booking(models.Model):

    EVENT_CHOICES = [
        ('Small Event', 'Small Event'),
        ('Medium Event', 'Medium Event'),
        ('Large Event', 'Large Event'),
    ]

    FOOD_CHOICES = [
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
    ]

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    palace = models.CharField(max_length=100)

    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    number_of_palace = models.PositiveIntegerField()

    food_type = models.CharField(max_length=50, choices=FOOD_CHOICES)

    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    event_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.event_date}"

from django.db import models

class StarterFood(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    details = models.TextField(blank=True)
    image = models.ImageField(upload_to='starter_foods/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
