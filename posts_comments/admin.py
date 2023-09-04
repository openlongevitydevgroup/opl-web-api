from django.contrib import admin

from .custom_admin.submission_admin import SubmissionAdmin
from .custom_admin.submission_references_admin import SubmissionReferenceAdmin
from .custom_admin.submitted_references_admin import SubmittedReferencesAdmin
from .models.comments import *
from .models.submissions import *


# Register your models here.
class CommentSubmissionAdmin(admin.ModelAdmin):
    readonly_fields = ["full_text"]


admin.site.register(Comment)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(SubmittedReferences, SubmittedReferencesAdmin)
admin.site.register(SubmissionReferences, SubmissionReferenceAdmin)
