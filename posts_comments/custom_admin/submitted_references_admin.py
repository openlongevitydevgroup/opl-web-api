from django.contrib import admin
from posts_comments.models.submissions import SubmittedReferences


######### ADMIN ACTION FOR ASSIGNING REFERENCES TO SUBMISSIONS FROM SUBMITTED REFERENCES -> SUBMISSION REFERENCES TABLE


class SubmittedReferencesAdmin(admin.ModelAdmin):
    list_display = ["ref_id", "type", "ref", "submission_id", "submission_full_text"]

    def submission_full_text(self, obj):  # Return the full text of the submission?
        return obj.submission.full_text
