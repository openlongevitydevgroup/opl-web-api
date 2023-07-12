from rest_framework import serializers
from models.submissions import Submission

class SubmissionSerializer(serializers.Serializer): 
    class Meta:
        model = Submission
        fields = ["submission_id", "date", "type", "full_text", "contact", "references" ]
