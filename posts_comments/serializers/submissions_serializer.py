from rest_framework import serializers
# from models.submissions import Submission
from posts_comments.models.submissions import Submission, SubmittedReferences, SubmissionReferences

# class SubmissionReferencesSerializerer(serializers.ModelSerializer): 
#     class Meta: 
#         model = SubmissionReferences
#         fields = ["submission_id", "reference_id"]

class SubmittedReferencesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = SubmittedReferences 
        fields = ["reference_id", "submission_id", "type", "ref"]

class SubmissionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Submission
        fields = ["submission_id", "created_at", "full_text", "contact", "submitted_references", "open_problem" , "first_name", "last_name", "affiliation"]

