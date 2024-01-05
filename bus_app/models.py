from enum import unique
from django.db import models


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # username = models.EmailField(unique=True, null=True)
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Bus(models.Model):
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    seats_available = models.IntegerField()
    stops = models.TextField()

class SeatBlock(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False)
    blocking_id = models.CharField(max_length=255, unique=True)
    pickup_point = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class Booking(models.Model):
    seat = models.ForeignKey(SeatBlock, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
