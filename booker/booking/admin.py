from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Slot)
admin.site.register(Country)
admin.site.register(Booking)

