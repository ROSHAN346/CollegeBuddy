from django.urls import path
from . import views

urlpatterns = [
  path('', views.scholarHome , name="scholar"),
  path('login/', views.login , name="scholar"),

]