
from django.urls import path
from ghostapp import views

urlpatterns = [
    path('', views.index),
]