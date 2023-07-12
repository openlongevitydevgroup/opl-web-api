from rest_framework import serializers
# from models.submissions import Submission
from posts_comments.models.submissions import Submission
from posts_comments.models.submissions import SubmissionReferences

class SubmissionReferencesSerialer(serializers.ModelSerializer): 
    class Meta: 
        model = SubmissionReferences
        fields = ["submission_id", "reference_id"]


class SubmissionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Submission
        fields = ["submission_id", "created_at", "type", "full_text", "contact", "submitted_references", "open_problem" ]
