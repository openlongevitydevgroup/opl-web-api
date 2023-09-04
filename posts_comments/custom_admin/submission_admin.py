from django.contrib import admin

from posts_comments.models.submissions import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Submission._meta.fields]
