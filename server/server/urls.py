from django.contrib import admin
from django.urls import path
from mathapp import views # type: ignore

urlpatterns = [
    path('',views.power, name='home'),
]
