from django.urls import path
from rental_connects.views import accounts

urlpatterns = [
    path("register/", accounts.register_view, name="register"),
    path("login/", accounts.login_view, name="login"),
    path("profile/", accounts.profile_view, name="profile"),
    path("dashboard/", accounts.dashboard_view, name="dashboard"),
    path('become_landlord/', accounts.become_landlord_view, name='become_landlord'),
]