from django.urls import path

from . import views

urlpatterns = [
    path("", views.contacts, name="contacts"),
    path("name/", views.name, name="name"),
    path("not-name/", views.not_name, name="not_name")
]