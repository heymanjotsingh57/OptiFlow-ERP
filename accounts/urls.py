from django.urls import path  # type: ignore
from . import views
from orders import views as order_views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # Public customer tracking
    path("track-order/", order_views.track_order, name="track_order"),
]