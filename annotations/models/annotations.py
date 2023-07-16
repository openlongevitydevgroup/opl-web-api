from django.db import models 
from .theory import Theory
from open_problems.models.references import Reference
from open_problems.models.open_problems import OpenProblem


# Abstract table that will link a problem to all annotations
class AnnotationsProblems(models.Model): 
    annotation_id = models.AutoField(primary_key=True)
    open_problem = models.ForeignKey(OpenProblem, on_delete=models.DO_NOTHING)
    class Meta: 
        abstract = True 

class AnnotationsReferences(models.Model):
    ref = models.OneToOneField(Reference, models.DO_NOTHING, db_column='Ref_id', primary_key=True)  # Field name made lowercase. The composite primary key (Ref_id, Theory_id) found, that is not supported. The first column is selected.
    theory = models.ForeignKey(Theory, models.DO_NOTHING, db_column='Theory_id', null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'theory_reference'
        unique_together = (('ref', 'theory'))