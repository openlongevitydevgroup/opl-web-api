from django.urls import path 
from questions import views
from questions.admin import QuestionsAdmin

urlpatterns = [
    path('questions/', views.questions_list), #All questions
    path('questions/root', views.questions_root),
    path('questions/<int:id>', views.question_detail), 
    path('questions/submit', views.submitted_questions),
    path('verify-token', views.verify_token)
]