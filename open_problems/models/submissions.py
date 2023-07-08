from django.db import models 
from .contacts_users import Contact 
class Submission(models.Model):
    submission_id = models.IntegerField() 
    title = models.CharField(max_length=300, null=True)
    full_text = models.TextField(null=True)
    # Are contacts required to submit ?? 

    def __str__(self) -> str:
        return f"{self.submission_id}: {self.title}"
    class Meta:
        abstract = True 

class ResearchSubmission(Submission): 
    ...

class SolutionSubmission(Submission): 
    ... 

class ResearchThread(models.Model): #Non cyclic table for now. 
    primary_submission = models.OneToOneField(ResearchSubmission)
    response_submission = models.ForeignKey(ResearchSubmission)

    def __str__(self) -> str: 
        return f"{self.primary_submission.submission_id} :  {self.response_submission.submission_id}"

class SolutionThread(models.Model):
    primary_submission = models.OneToOneField(SolutionSubmission)
    response_submission = models.ForeignKey(SolutionSubmission)

    def __str__(self) -> str:
        return f"{self.primary_submission.submission_id} : {self.response_submission.submission_id}"