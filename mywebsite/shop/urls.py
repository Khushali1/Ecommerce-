from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutAs"),
    path("contact/", views.contact, name="ContactUs"),
    path("Tracker/", views.tracker, name="TrackingStatus"),
    path("Search/", views.Search, name="Search"),
    path("Products/", views.ProductView, name="ProductView"),
    path("Checkout/", views.Checkout, name="checkout"),

]