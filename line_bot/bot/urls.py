from django.urls import path
from . import views

urlpatterns = [
    path('lb/webhook', views.index, name='lb-webhook'),
]