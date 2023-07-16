from django.contrib import admin
from .models.annotations import AnnotationsProblems
from .models.theory import Theory, TheoryProblem 
from .models.species import Species
from .models.genes import Gene, GeneProblem
# Register your models here.

# class AnnotationsProblemsAdmin(admin.ModelAdmin): 
#     list_display = [field.name for field in AnnotationsProblems._meta.fields]
    
admin.site.register(Theory)
admin.site.register(TheoryProblem)
admin.site.register(Species)
admin.site.register(Gene)
admin.site.register(GeneProblem)