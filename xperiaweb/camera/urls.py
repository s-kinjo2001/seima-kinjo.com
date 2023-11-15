from django.urls import path
from . import views

urlpatterns = [
    path('kaito/', views.kaito, name="kaito"),
]