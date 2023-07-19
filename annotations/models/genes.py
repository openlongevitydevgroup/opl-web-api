from django.db import models 
from .species import Species
from .annotations import AnnotationsProblems

class Gene(models.Model): 
    gene_id = models.AutoField(primary_key=True)
    gene_name = models.CharField(max_length=50, unique=True)
    gene_symbol = models.CharField(max_length=10, unique=True)
    species = models.ForeignKey(Species, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.gene_symbol}: {self.gene_name}"

    class Meta: 
        db_table = "Genes"
        db_table_comment = "Table for all genes"

class GeneProblem(AnnotationsProblems):
    gene_id = models.ForeignKey(Gene, on_delete=models.CASCADE) 
    def __str__(self) -> str:
        return f"{self.gene.gene_id}: {self.open_problem.open_problem_id} "
    class Meta:
        db_table_comment = "Relation table for each gene and open problem"
