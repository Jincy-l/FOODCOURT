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
