from django.urls import path 
from open_problems import views
from open_problems.admin import OPAdmin

urlpatterns = [
    path('open-problems/', views.questions_list), #All questions
    path('open-problems/root', views.questions_root),
    path('open-problems/<int:id>', views.question_detail), 
    path('open-problems/submit', views.submitted_questions),
    path('verify-token', views.verify_token)
]