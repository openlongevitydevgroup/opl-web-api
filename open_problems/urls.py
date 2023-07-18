from django.urls import path 
from open_problems import views

urlpatterns = [
    path('', views.questions_list), #All questions
    path('root', views.questions_root),
    path('<int:id>', views.question_detail), 
    path('submit', views.submitted_questions),
    path('verify-token', views.verify_token), 
    path("<int:id>/references", views.get_references)
]