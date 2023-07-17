from django.db import models
from .contacts_users import Contact
from .references import Reference


class OpenProblem(models.Model):
    problem_id = models.AutoField(
    primary_key=True, serialize=True, default=None)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    contact = models.OneToOneField(
        Contact, null=True, on_delete=models.SET_NULL, blank=True)
    reference = models.ForeignKey(
        Reference, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class OpenProblems(OpenProblem):
    parent_problem = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    class Meta:
        db_table = 'OpenProblems'
        db_table_comment = 'These are the current open problems that we have accepted from the submitted questions'

    def __str__(self):
        return f'{self.question_id}: {self.title}'


class SubmittedProblems(OpenProblem):
    parent_problem = models.ForeignKey(
        OpenProblems, null=True, blank=True, on_delete=models.SET_NULL)
    species = models.CharField(max_length=50, null=True, blank=True)
    citation = models.TextField(blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    job_field = models.CharField(max_length=100, blank=True)
    organisation = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.title} : {self.email}"
        

    class Meta:
        db_table = 'Submitted-OP'
        db_table_comment = 'These are the submitted questions from users that will undergo review'



class ProblemRelation(models.Model):
    QR_id = models.AutoField(primary_key=True)
    QR_title = models.CharField(max_length=100)
    QR_description = models.TextField(blank=True)

    class Meta:
        db_table = "Open-relations"
        db_table_comment = 'This contains information about how a question/submitted question is related to a question'


class RelatedProblem(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(
        OpenProblems, on_delete=models.SET_NULL, null=True, related_name='parent_relation')
    child_id = models.ForeignKey(
        OpenProblems, on_delete=models.SET_NULL, null=True, related_name='child_relation')
    relation_rate = models.IntegerField(null=True, blank=True)
    QR_id = models.ForeignKey(
        ProblemRelation, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "Related-problems"
        db_table_comment = "This contains the parent-child relationships between questions. Hierarchical data."

    def __str__(self) -> str:
        return f'{self.id}: {self.parent_id.title} && {self.child_id.title}'


class QuestionReference(models.Model):
    question_id = models.ForeignKey(
        OpenProblems, on_delete=models.SET_NULL, null=True)
    reference_id = models.ForeignKey(
        Reference, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "OP-references"
        db_table_comment = "Table containing which references are tied to which questions"

