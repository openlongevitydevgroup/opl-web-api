from django.contrib import admin
from .models.submissions import * 
from .models.comments import *
# Register your models here.

class CommentSubmissionAdmin(admin.ModelAdmin): 
    readonly_fields = ["full_text"]


admin.site.register(Comment)
admin.site.register(Submission,CommentSubmissionAdmin)
admin.site.register(SubmittedReferences)

