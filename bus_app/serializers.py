from dataclasses import field, fields
from pyexpat import model
from django.forms import fields_for_model
from rest_framework import serializers
from .models import Bus, CustomUser, SeatBlock, Booking, CustomUser
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name','last_name','email','phone_number','address','password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

        
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class SeatBlockSerializer(serializers.Serializer):
    bus_start_time = serializers.DateTimeField()
    pickup_point = serializers.CharField()
    num_passengers = serializers.IntegerField()
    created_at = serializers.DateTimeField(default=timezone.now, read_only=True)
        

class BookingSerializer(serializers.Serializer):
    blocking_id = serializers.CharField()
    created_at = serializers.DateTimeField(default=timezone.now, read_only=True)
    
    