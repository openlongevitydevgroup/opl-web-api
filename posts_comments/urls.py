from django.urls import path
from posts_comments.views.submission_view import get_posts, get_posts_counts, submit_post, get_post
from posts_comments.views.comment_view import get_comments, get_single_comment, post_comment
from posts_comments.views.verify_references_view import verify_reference

urlpatterns = [
    path("<int:id>/", get_posts),
    path("<int:id>/counts", get_posts_counts),
    path("<int:id>/submit", submit_post),
    path("get/<int:id>", get_post),
    path("get/<int:id>/comments", get_comments),
    path("get/<int:post_id>/<int:comment_id>", get_single_comment),
    path("post/<int:post_id>/comment/submit", post_comment),
    path("post/verify-reference", verify_reference)
]
