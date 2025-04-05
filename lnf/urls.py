from django.urls import path
from . import views

urlpatterns = [
  path('', views.lnfHome , name="LostNFound"),
  path('info/' , views.info , name="FindInfo"),
  path('report/' , views.report_lost_item , name="ReportChize"),
  path('view-items/', views.view_lost_items, name='view_items'),
]