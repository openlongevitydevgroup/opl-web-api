from django.urls import path 
from posts_comments.views.submission_view import get_posts, get_posts_counts, submit_post, get_post
from posts_comments.views.comment_view import get_comments, get_single_comment
urlpatterns = [
    path("<int:id>/", get_posts),
    path("<int:id>/counts", get_posts_counts),
    path("<int:id>/submit", submit_post),
    path("get/<int:id>", get_post),
    path("get/<int:id>/comments", get_comments),
    path("get/comments/<int:id>", get_single_comment)
]