from django.urls import path
from . import views

urlpatterns = [
    # Homepage for the canteen
    path('', views.canteen, name="Canteen"),

    # AI meal suggestion page
    path('mealAI/', views.index, name='index'),
    
    # API endpoints
    path('api/analyze/', views.analyze_food, name='analyze_food'),  # Analyze food data
    path('api/feedback/', views.submit_feedback, name='submit_feedback'),  # Submit user feedback
    path('api/feedback/stats/', views.feedback_stats, name='feedback_stats'),  # View feedback statistics
]
