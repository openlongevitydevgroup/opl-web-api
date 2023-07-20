from rest_framework import serializers
from models.comments import Comments

class CommentsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comments 
        fields = ["comment_id", "full_text", "question", "parent"]
