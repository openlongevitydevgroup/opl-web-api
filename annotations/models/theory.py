from django.db import models 

from open_problems.models import OpenProblems
from open_problems.models import Reference

#Theory models to attach for a particular open problem. 
class Theory(models.Model):
    theory_id = models.AutoField(db_column='Theory_id', primary_key=True)  # Field name made lowercase.
    theorytitle = models.CharField(db_column='TheoryTitle', max_length=40, blank=True, null=True)  # Field name made lowercase.
    theorydesc = models.TextField(db_column='TheoryDesc', blank=True, null=True)  # Field name made lowercase.
    parent_t_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
# end of edit by Hamid
    class Meta:
        db_table = 'Theory'
    def __str__(self) -> str:
        return f"{self.theory_id}: {self.theorytitle}"
    


class TheoryProblem(models.Model):
    opinion = models.OneToOneField(OpenProblems, on_delete=models.DO_NOTHING, primary_key=True)  # Field name made lowercase. The composite primary key (Opinion_id, species_id, Theory_id) found, that is not supported. The first column is selected.
    species_id = models.BigIntegerField()
    theory_id = models.ForeignKey(Theory, on_delete=models.DO_NOTHING, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'theory_question'
        unique_together = (('opinion', 'species_id', 'theory_id'),)


class TheoryReference(models.Model):
    ref = models.OneToOneField(Reference, models.DO_NOTHING, db_column='Ref_id', primary_key=True)  # Field name made lowercase. The composite primary key (Ref_id, Theory_id) found, that is not supported. The first column is selected.
    theory = models.ForeignKey(Theory, models.DO_NOTHING, db_column='Theory_id', null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'theory_reference'
        unique_together = (('ref', 'theory'))
