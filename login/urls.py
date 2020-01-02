from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, complete_register


urlpatterns = [
    path('',  LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('register/',  register, name="register"),
    path('registerfull/', complete_register, name="complete_register"),
]
