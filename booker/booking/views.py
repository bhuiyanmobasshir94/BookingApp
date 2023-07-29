from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


# Create your views here.
class SlotPageView(TemplateView):
    template_name = "slot.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slots"] = Slot.objects.all()
        return context
