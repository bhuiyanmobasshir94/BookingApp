from django.urls import path

from .views import *

urlpatterns = [
    path("", SlotPageView.as_view()),

]