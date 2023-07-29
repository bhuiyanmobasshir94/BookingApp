import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CheckConstraint, F, Q
from django.utils.translation import gettext_lazy as _

# Create your models here.



class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Slot(BaseModel):
    user = models.ForeignKey(User, related_name='user_slots', on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, verbose_name=_("Slot Date"))
    start_time = models.TimeField(null=False, blank=False, verbose_name=_("Slot Start Time"))
    end_time = models.TimeField(null=False, blank=False, verbose_name=_("Slot End Time"))
    is_booked = models.BooleanField(default=False, verbose_name=_("Is Booked"))

    def __str__(self) -> str:
        return f"Date: {str(self.date)}, Time: {str(self.start_time)} to {str(self.end_time)}, Booked: {self.is_booked}"
    class Meta:
        verbose_name = "Slot"
        constraints = [
            CheckConstraint(
                check = Q(end_time__gt=F('start_time')), 
                name = 'check_slot-time',
            ),
            models.UniqueConstraint(
                fields=["date", "start_time", "end_time"],
                name="unique_booking_date_time",
            ),

        ]

class Country(BaseModel):
    name = models.CharField(
        max_length=50, verbose_name=_("Name"), null=False, blank=False
    )
    code = models.CharField(
        max_length=5, verbose_name=_("Code"), null=False, blank=False
    )

    def __str__(self) -> str:
        return f"Country: {self.name}, Code: {self.code}"

    class Meta:
        verbose_name = "Country"


class Booking(BaseModel):
    slot = models.ForeignKey(Slot, related_name='slot_bookings', on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100, verbose_name=_("Name"), null=False, blank=False
    )
    address = models.TextField(blank=False, null=False, verbose_name=_("Address"))
    phone = models.CharField(
        max_length=100, verbose_name=_("Phone"), null=False, blank=False
    )
    country = models.ForeignKey(Country, related_name='slot_countries', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Name: " + self.name + " Slot: " + str(self.slot)
    
    class Meta:
        verbose_name = "Booking"

