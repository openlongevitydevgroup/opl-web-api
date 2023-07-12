from django.db import models
class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True) 
    question = models.ForeignKey(OpenProblems, null=False, blank=False, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
    full_text = models.TextField(blank=False, null=False)