from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registerView, complete_registerView

urlpatterns = [
    path('',  LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
    path('register/', registerView.as_view(), name="register"),
    path('registerfull/', complete_registerView.as_view(), name="complete_register"),
]
