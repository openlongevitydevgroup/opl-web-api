from django.contrib import admin

from posts_comments.models.submissions import SubmittedReferences
from open_problems.models.references import  Reference
from crossref.restful import Works


######### ADMIN ACTION FOR ASSIGNING REFERENCES TO SUBMISSIONS FROM SUBMITTED REFERENCES -> SUBMISSION REFERENCES TABLE
def create_reference(modeladmin, queryset, request):
    for reference in queryset:
        ...






##### CUSTOM CLASS
class SubmittedReferencesAdmin(admin.ModelAdmin):
    list_display = ["reference_id", "type", "ref", "submission_id", "submission_full_text"]


    def submission_full_text(self, obj):  # Return the full text of the submission?
        return obj.submission_id.full_text
