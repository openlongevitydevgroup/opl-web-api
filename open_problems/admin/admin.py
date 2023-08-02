from open_problems.models.open_problems import RelatedProblem, ProblemReference, Reference, Contact
from open_problems.models.references import Journal, RefType
from django.contrib import admin

# Registering models to admin without class created.
admin.site.register(RelatedProblem)
admin.site.register(Reference)
admin.site.register(Journal)
admin.site.register(RefType)
admin.site.register(Contact)
admin.site.register(ProblemReference)
