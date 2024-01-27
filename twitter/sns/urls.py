from django.urls import include, path
from . import views

app_name= "sns"
urlpatterns = [
    path('home/', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
]