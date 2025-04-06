from django.urls import path
from . import views

urlpatterns = [
  path('', views.scholarHome , name="scholar"),
    path('login/', views.login, name="login"),
    # path('save/' , views.saveToDB , name="user"),
    path('dash/' , views.renderPage , name='dash')
]