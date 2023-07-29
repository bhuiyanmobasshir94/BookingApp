from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView
from .models import *


# Create your views here.
# class SlotPageView(TemplateView):
#     template_name = "slot.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["slots"] = Slot.objects.all()
#         return context

def slots(request):
    slots = Slot.objects.all()
    if request.method == 'POST':
        slot_id = request.POST.get('slot_id')
        return HttpResponseRedirect(f'/booking/{slot_id}')
    return render(request, 'slot.html', {'slots': slots}) 

def book_slot(request, pk):
    slot = Slot.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        country_code = request.POST.get('country_code')
        country = Country.objects.get(code=country_code.upper())
        booking = Booking.objects.create(slot=slot, name=name, address=address, phone=phone_number, country=country)
        booking.save()
        slot.is_booked = True
        slot.save()
        return HttpResponseRedirect('/')
        # return HttpResponse(f"Booking successful! Your booking ID is {booking.id}")
    return render(request, 'book.html', {'slot': slot})