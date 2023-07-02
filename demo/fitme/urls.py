from django.urls import path
from fitme import views

urlpatterns = [
    path('', views.home, name='home')
]