# BusTicketingSystem REST API

This is a online Bus ticket application providing a REST
API to Book a ticket for Bus.

# Bus	Search
  `Bus	search	should	take	input – source, destination,	date	of	journey.`
  `Bus	search	should	return	– Buses	available	along	with	start	time	of	bus,	
  no	 of	 seats	 available	 in	 that	 bus	 and	 stops	 between	 source	 and	
  destination`
# Block	seats
`Blocking	of	seats	should	take	input	– No	of	passengers,	Bus (based	of	
start	time),	pickup	point	(one	of	the	stops	in	the	route)`
`Blocking	of	seats	should	return	confirmation	along	with	blocking	id.`

# Book	tickets
`Booking	tickets	should	take	input	– Blocking	id`.
`Booking	ticket should	return	confirmation	message	along	with	Booking	
id`.

## Install the dependencies

    pip install -r reuirement.txt

## Run the Database migrations
  python manage.py makemigrations
  python manage.py migrate
  
## Run the app
  python manage.py runserver 0.0.0.0:8080

# REST API

The REST API to BusTicketingSystem app is described below.

## Register a User

### Request

`Post /register/`

curl --location '127.0.0.1:8000/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name":"rachit",
    "last_name":"kumar",
    "email":"vashu@gmail.com",
    "phone_number":"9354081327",
    "address":"Saharanpur",
    "password":"12345"
}'

### Response

    [{
    "id": 4,
    "first_name": "rachit",
    "last_name": "kumar",
    "email": "vashu@gmail.com",
    "phone_number": "9354081327",
    "address": "Saharanpur"}
    ]

## Login User

### Request

`POST /login/`

curl --location '127.0.0.1:8000/login/' --header 'Content-Type: application/json' \
--data-raw '{
    "email":"vashu@gmail.com",
    "password":"12345"
}'

### Response

    {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzExMTMyMiwiaWF0IjoxNzA0NTE5MzIyLCJqdGkiOiJlMTUzNTRmZWI0MTk0N2FmYTZjMzg5NmQ0MTI3ZjA5MiIsInVzZXJfaWQiOjR9.3PlXARqtYjuo3HbpiXVXcCMRfTGvqyuroA3fheWUF-o",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0NTE5NjIyLCJpYXQiOjE3MDQ1MTkzMjIsImp0aSI6IjAwZGFlNGE3Y2Y4YTQwOTJiMTk1NDk0NTU0ZTU5ZjQwIiwidXNlcl9pZCI6NH0.kkiJiAqMkdKVe63h_SudasHmr_HwN1K2dT_ey7ls60c",
    "message": "Succssfully login"
}
## Search a Bus
### Request

`GET /bus-search?source=Saharanpur&destination=Delhi&date_of_journey=2024-01-06`

    curl --location '127.0.0.1:8000/bus-search?source=Saharanpur&destination=Delhi&date_of_journey=2024-01-06' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0NTE5NjIyLCJpYXQiOjE3MDQ1MTkzMjIsImp0aSI6IjAwZGFlNGE3Y2Y4YTQwOTJiMTk1NDk0NTU0ZTU5ZjQwIiwidXNlcl9pZCI6NH0.kkiJiAqMkdKVe63h_SudasHmr_HwN1K2dT_ey7ls60c' \
--data ''

### Response

  
    {
        "id": 1,
        "source": "Saharanpur",
        "destination": "Delhi",
        "start_time": "2024-01-06T18:00:00Z",
        "seats_available": 15,
        "stops": "Nanauta\r\nShamli\r\nLoni\r\nShadhara\r\nDelhi"
    }

## Block Seat

### Request

`GET /seat-block/`

    curl --location '127.0.0.1:8000/seat-block/' \
  --header 'Content-Type: application/json' \
  --data '{
      "bus_start_time":"2024-01-06T06:00:00Z",
      "num_passengers":"5",
      "pickup_point":"Nanauta"
  }'

### Response

    {'message': 'Seats blocked successfully.', 'blocking_id': 'BLOCK-2024-01-06T06:00:00Z-Nanauta'}

## Booking a ticket

### Request

`POST /book-ticket/`

    curl --location '127.0.0.1:8000/book-ticket/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0NTE5NjIyLCJpYXQiOjE3MDQ1MTkzMjIsImp0aSI6IjAwZGFlNGE3Y2Y4YTQwOTJiMTk1NDk0NTU0ZTU5ZjQwIiwidXNlcl9pZCI6NH0.kkiJiAqMkdKVe63h_SudasHmr_HwN1K2dT_ey7ls60c' \
    --data '{
           "blocking_id": "BLOCK-2024-01-06T06:00:00Z-Nanauta"
    }'

### Response

    {'message': 'Booking successful.', 'booking_id': 'BOOK-BLOCK-2024-01-06T06:00:00Z-Nanauta'}

