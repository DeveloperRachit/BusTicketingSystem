from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, BusSearchAPIView, BlockSeatsAPIView, BookingTicketAPIView



urlpatterns = [
    # path('user-registration/', user_registration, name='user_registration'),

    path('bus-search/', BusSearchAPIView.as_view(), name='bus_search'),
    path('seat-block/', BlockSeatsAPIView.as_view(), name='seat_block'),
    path('book-ticket/', BookingTicketAPIView.as_view(), name='book_ticket'),
    
    # path('view-bookings/', view_bookings, name='view_bookings'),

    

    path('register/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
]
