from django.urls import path

from .views import *

urlpatterns = [
    path("",slots),
    path("booking/<uuid:pk>/", book_slot)
]