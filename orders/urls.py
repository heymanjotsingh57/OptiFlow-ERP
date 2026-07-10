from django.urls import path
from . import views

urlpatterns = [

    # Dashboard
    path("", views.home, name="home"),

    # Customer Management
    path("add/", views.add_customer, name="add_customer"),

    path("edit/<int:id>/", views.edit_customer, name="edit_customer"),

    path("delete/<int:id>/", views.delete_customer, name="delete_customer"),

    # Billing & Receipt
    path("receipt/<int:id>/", views.receipt, name="receipt"),

    # Customer Order Tracking
    path("track-order/", views.track_order, name="track_order"),

]