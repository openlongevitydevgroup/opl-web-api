from django.db import models

# class Species(models.Model):
#     species_id = models.AutoField(primary_key=True, serialize=True)
#     species_name = models.CharField(max_length= 100) 

# #Tables about the different information about subquestions. 
# class Citation(models.Model):
#     citation_id = models.AutoField(primary_key=True, serialize=True)
#     full_citation = models.CharField(max_length=200)
#     #For now it's not necessary to split the referece information so we'll keep the full citation in one column

# #A table containing all the questions 
# class Question(models.Model):
#     class Meta:
#         abstract = True
#     question_id = models.AutoField(primary_key=True, serialize=True, default=None)
#     title = models.CharField(max_length=200, blank=True)
#     excerpt = models.TextField(blank=True)
#     #Foreign keys from other tables 
#     species = models.ForeignKey(Species, on_delete=models.SET_NULL , null=True, blank=True)
#     citation = models.ForeignKey(Citation, on_delete=models.SET_NULL, null=True, blank=True)

# class CurrentQuestions(Question): 
#     parent_question = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

#     def __str__(self):
#         return f'{self.question_id}: {self.title}'

# class SubmittedQuestions(Question):
#     parent_question = models.ForeignKey(CurrentQuestions, on_delete=models.SET_NULL, null=True)
#     species = models.CharField(max_length=100, null=True, blank=True)
#     citation = models.CharField(max_length=500, null=True, blank=True)
#     def __str__(self): 
#         return f'{self.question_id}: {self.title}'

