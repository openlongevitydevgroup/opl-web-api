from rest_framework import serializers
from posts_comments.models.submissions import (
    Submission,
    SubmittedReferences,
    SubmissionReferences,
)


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            "submission_id",
            "created_at",
            "full_text",
            "contact",
            "submitted_references",
            "open_problem",
            "first_name",
            "last_name",
            "affiliation",
        ]


class SubmissionReferencesSerializer(serializers.ModelSerializer):
    references = serializers.SerializerMethodField()

    class Meta:
        model = SubmissionReferences
        fields = ["submission_id", "reference_id", "references"]

    def get_references(self, obj):
        reference = obj.reference_id
        return {
            "id": reference.ref_id,
            "full_citation": reference.full_citation,
        }  # For now we only need this information


class SubmittedReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedReferences
        fields = ["reference_id", "submission_id", "type", "ref"]
