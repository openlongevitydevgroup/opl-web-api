from django.db import models
from models import Species, Citation
from contacts_users import Contact 

class Question(models.Model):
    class Meta:
        abstract = True
    question_id = models.AutoField(
        primary_key=True, serialize=True, default=None)
    title = models.CharField(max_length=200, blank=True)
    excerpt = models.TextField(blank=True)
    # Foreign keys from other tables
    contact = models.OneToOneField(null=True, blank=True)
    species = models.ForeignKey(
        Species, on_delete=models.SET_NULL, null=True, blank=True)
    citation = models.ForeignKey(
        Citation, on_delete=models.SET_NULL, null=True, blank=True)


class Questions(Question):
    class Meta:
        db_table = 'Current-questions'
        db_table_commennt = 'These are the current questions that we have accepted from the submitted questions'
    
    def __str__(self):
        return f'{self.id}: {self.title}'


class SubmittedQuestions(Question):
    parent_question_id = models.ForeignKey(blank=True, null=True)
    class Meta:
        db_table = 'Submitted-questions'
        db_table_comment = 'These are the submitted questions from users that will undergo review'


class QuestionRelation(models.Model):
    QR_id = models.AutoField(primary_key=True)
    QR_title = models.CharField(max_length=100)
    QR_description = models.TextField(blank=True)

    class Meta:
        db_table = "Question-relations"
        tb_table_comment = 'This contains information about how a question/submitted question is related to a question'


class RelatedQuestions(models.Model):
    related_question_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Questions)
    submitted_question_id = models.ForeignKey(SubmittedQuestions)
    relation_rate = models.IntegerField(null=True, blank=True)
    QR_id = models.ForeignKey(QuestionRelation)

    class Meta:
        db_table = "Related-questions"

        tb_table_comment = "This contains the parent-child relationships between questions. Hierarchical data."
