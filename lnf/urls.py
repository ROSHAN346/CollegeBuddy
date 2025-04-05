from django.urls import path
from . import views

urlpatterns = [
  path('', views.lnfHome , name="LostNFound"),
]