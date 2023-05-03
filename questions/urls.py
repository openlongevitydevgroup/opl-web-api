from django.urls import path 
from questions import views 

urlpatterns = [
    path('questions/', views.questions_lists), 
    path('questions/<int:id>', views.question_detail_single), 
    path('questions/submit', views.submitted_questions),
    path('questions/recursive', views.recursive_questions)
]