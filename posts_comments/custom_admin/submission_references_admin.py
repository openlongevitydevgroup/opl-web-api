from django.contrib import admin
from posts_comments.models.submissions import SubmissionReferences


### Customm admin class for Submissions and their references
class SubmissionReferenceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SubmissionReferences._meta.fields]


