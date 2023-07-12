from django.db import models
from open_problems.models.contacts_users import Contact
from open_problems.models.open_problems import OpenProblems


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    full_text = models.TextField(null=True)
    question = models.ForeignKey(OpenProblems, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, blank=True, null=True)
    references = models.TextField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    # Are contacts required to submit ??
    class Meta:
        abstract = True

    

class ResearchSubmission(Submission):
    parent = models.ForeignKey("self", null=True, on_delete=models.DO_NOTHING)
    
    class Meta:
        ordering = ["date"]
    def __str__(self) -> str:
        return f"{self.submission_id}: {self.question}"



class SolutionSubmission(Submission):
    parent = models.ForeignKey("self", null=True, on_delete=models.DO_NOTHING)

    class Meta: 
        ordering = ["date"]
    def __str__(self) -> str:
        return f"{self.submission_id}: {self.question}"



