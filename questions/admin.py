from .models.questions import Questions, SubmittedQuestions
from .models.references import Reference, Author, Journal, RefType
from django.contrib import admin

# Register your models here.
admin.site.register(Questions)
admin.site.register(SubmittedQuestions)
admin.site.register(Reference)
admin.site.register(Journal)
admin.site.register(RefType)

