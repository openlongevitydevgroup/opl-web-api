from django.urls import path 
from questions import views 

urlpatterns = [
    path('questions/', views.questions_list), #All questions
    path('questions/root', views.questions_root),
    path('questions/<int:id>', views.question_detail), 
    path('questions/submit', views.submitted_questions),
    # path('questions/recursive', views.recursive_questions)
]