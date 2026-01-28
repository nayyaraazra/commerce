from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"), # route the login
    path("logout", views.logout_view, name="logout"), # route the logout
    path("register", views.register, name="register")
]
