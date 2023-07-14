from django.contrib import admin
from .models.submissions import * 
from .models.comments import *
# Register your models here.

class SubmissionAdmin(admin.ModelAdmin): 
    readonly_fields = ["full_text"]

admin.site.register(Submission,SubmissionAdmin)
admin.site.register(SubmittedReferences)

