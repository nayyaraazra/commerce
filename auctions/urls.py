from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"), # route the login
    path("logout", views.logout_view, name="logout"), # route the logout
    path("register", views.register, name="register"),
    path("listings/<int:listing_id>/", views.listing_detail, name="listing_detail"),
    # path("listing/<int:listing_id>/", views.listing_detail, name="listing_detail"),
    path("create", views.create_listing, name="create_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/<int:listing_id>/", views.toggle_watchlist, name = "toggle_watchlist")
]
