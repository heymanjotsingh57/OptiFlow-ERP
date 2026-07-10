from django.contrib import admin  # type: ignore[import]
from .models import Order

admin.site.register(Order)