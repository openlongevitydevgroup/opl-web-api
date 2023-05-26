from django.db import models
from .contacts_users import Contact
from .species import Species
from .references import Reference


class Question(models.Model):
    class Meta:
        abstract = True
    question_id = models.AutoField(
        primary_key=True, serialize=True, default=None)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Foreign keys from other tables
    contact = models.OneToOneField(
        Contact, null=True, on_delete=models.SET_NULL, blank=True)
    species = models.ForeignKey(
        Species, on_delete=models.SET_NULL, null=True, blank=True)
    reference = models.ForeignKey(
        Reference, on_delete=models.SET_NULL, null=True, blank=True)


class Questions(Question):
    class Meta:
        db_table = 'Current-questions'
        db_table_comment = 'These are the current questions that we have accepted from the submitted questions'

    def __str__(self):
        return f'{self.question_id}: {self.title}'


class SubmittedQuestions(Question):
    parent_question = models.OneToOneField(Questions,null=True, blank=True, on_delete=models.SET_NULL)
    class Meta:
        db_table = 'Submitted-questions'
        db_table_comment = 'These are the submitted questions from users that will undergo review'


class QuestionRelation(models.Model):
    QR_id = models.AutoField(primary_key=True)
    QR_title = models.CharField(max_length=100)
    QR_description = models.TextField(blank=True)

    class Meta:
        db_table = "Question-relations"
        db_table_comment = 'This contains information about how a question/submitted question is related to a question'


class RelatedQuestions(models.Model):
    related_question_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(
        Questions, on_delete=models.SET_NULL, null=True)
    submitted_question_id = models.ForeignKey(
        SubmittedQuestions, on_delete=models.SET_NULL, null=True)
    relation_rate = models.IntegerField(null=True)
    QR_id = models.ForeignKey(
        QuestionRelation, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Related-questions"
        db_table_comment = "This contains the parent-child relationships between questions. Hierarchical data."


class QuestionReference(models.Model):
    question_id = models.ForeignKey(
        Questions, on_delete=models.SET_NULL, null=True)
    reference_id = models.ForeignKey(
        Reference, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "Questions-references"
        db_table_comment = "Table containing which references are tied to which questions"
