from django.urls import path 
from posts_comments import views

urlpatterns = [
    path("<int:id>/", views.get_posts),
    path("<int:id>/counts", views.get_posts_counts),
    path("<int:id>/submit", views.submit_post),
    path("get/<int:id>", views.get_post),
]