from myapp import views
from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('factorial/',views.factorial),


]