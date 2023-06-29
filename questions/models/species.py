from django.db import models 

class Species(models.Model): 
    species_id = models.AutoField(primary_key=True) 
    genus = models.CharField(max_length=50, null=True)
    species = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.genus} {self.species}'
    
    class Meta: 
        db_table = "Species"

