

from django.urls import path

from . import views
app_name = 'public'
urlpatterns = [

    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("appointments", views.appointments, name="appointments"),
    path("map", views.s, name="map"),


]
