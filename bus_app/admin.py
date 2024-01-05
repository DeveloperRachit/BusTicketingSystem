from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(SeatBlock)
admin.site.register(Booking)
admin.site.register(Bus)
