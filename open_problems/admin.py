from open_problems.models.open_problems import RelatedProblem, ProblemReference, Reference, Contact, OpenProblems, \
    SubmittedProblems
from open_problems.models.references import Journal, RefType
from open_problems.custom_admin_classes.open_problems_admin import OPAdmin
from open_problems.custom_admin_classes.submitted_problems_admin import SubmittedProblemsAdmin
from django.contrib import admin

# Registering models to admin without class created.

admin.site.register(OpenProblems, OPAdmin)
admin.site.register(SubmittedProblems, SubmittedProblemsAdmin)
admin.site.register(RelatedProblem)
admin.site.register(Reference)
admin.site.register(Journal)
admin.site.register(RefType)
admin.site.register(Contact)
admin.site.register(ProblemReference)
