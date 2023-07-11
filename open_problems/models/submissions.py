from django.db import models
from .contacts_users import Contact
from .references import Reference
from .open_problems import OpenProblems


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    full_text = models.TextField(null=True)
    question = models.ForeignKey(OpenProblems, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING, blank=True, null=True)

    # Are contacts required to submit ??
    class Meta:
        abstract = True


class ResearchSubmission(Submission):
    parent = models.ForeignKey("self", null=True, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.submission_id}: {self.question}"


class SolutionSubmission(Submission):
    parent = models.ForeignKey("self", null=True, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.submission_id}: {self.question}"


class ResearchThread(models.Model):  # Non cyclic table for now.
    primary_submission = models.OneToOneField(ResearchSubmission)
    response_submission = models.ForeignKey(ResearchSubmission)

    def __str__(self) -> str:
        return f"{self.primary_submission.submission_id} :  {self.response_submission.submission_id}"


class SolutionThread(models.Model):
    primary_submission = models.OneToOneField(SolutionSubmission)
    response_submission = models.ForeignKey(SolutionSubmission)

    def __str__(self) -> str:
        return f"{self.primary_submission.submission_id} : {self.response_submission.submission_id}"
