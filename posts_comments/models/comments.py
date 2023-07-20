from django.db import models
from open_problems.models.open_problems import OpenProblems
from posts_comments.models.submissions import Submission

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True) 
    submission = models.ForeignKey(Submission, on_delete=models.DO_NOTHING)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    full_text = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.comment_id}:{self.full_text}"
