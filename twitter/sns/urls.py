from django.urls import include, path
from . import views

app_name= "sns"
urlpatterns = [
    path('', views.top, name='top'),
    path('home/', views.index, name='index'),
]