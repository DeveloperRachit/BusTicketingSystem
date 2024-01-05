from sre_constants import SUCCESS
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Bus, SeatBlock, Booking
from django.contrib.auth import authenticate, login
from .serializers import BusSerializer, SeatBlockSerializer, BookingSerializer, UserSerializer
from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email = email).first()
        if user is None:
            raise AuthenticationFailed("User not Found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh":str(refresh),
            "access":str(refresh.access_token),
            "message":"Succssfully login"
        })


class BusSearchAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        source = request.query_params.get("source")
        destination = request.query_params.get("destination")
        date_of_journey = request.query_params.get("date_of_journey")
        buses = Bus.objects.filter(source=source, destination=destination, start_time__date=date_of_journey)
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data)
    

class BlockSeatsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SeatBlockSerializer(data=request.data)
        if serializer.is_valid():
            bus_start_time = serializer.validated_data['bus_start_time']
            pickup_point = serializer.validated_data['pickup_point']
            num_passengers = serializer.validated_data['num_passengers']
            bus = Bus.objects.get(start_time=bus_start_time) 
            blocking_id = f'BLOCK-{bus_start_time}-{pickup_point}'  # Generate a blocking ID
            SeatBlock.objects.create(bus=bus,is_blocked=True,blocking_id=blocking_id,pickup_point=pickup_point)
            return Response({'message': 'Seats blocked successfully.', 'blocking_id': blocking_id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingTicketAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            blocking_id = serializer.validated_data['blocking_id']
            booking_id = f'BOOK-{blocking_id}'  # Generate a booking ID
            block_seat = SeatBlock.objects.get(blocking_id=blocking_id)
            Booking.objects.create(seat=block_seat, booking_id=booking_id)
            return Response({'message': 'Booking successful.', 'booking_id': booking_id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
