from django.contrib import admin
from .models.annotations import AnnotationsProblems
from .models.theory import Theory, TheoryProblem 
from .models.species import Species
from .models.genes import Gene, GeneProblem
# Register your models here.

class TheoryProblemAdmin(admin.ModelAdmin): 
    list_fields = ["theory_title", "problem_title"]

admin.site.register(Theory)
admin.site.register(TheoryProblem, TheoryProblemAdmin)
admin.site.register(Species)
admin.site.register(Gene)
admin.site.register(GeneProblem)