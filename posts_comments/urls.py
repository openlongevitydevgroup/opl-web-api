from django.urls import path 
from posts_comments import views

urlpatterns = [
    path("<int:id>/", views.get_posts),
    path("<int:id>/submit", views.submit_post)
]