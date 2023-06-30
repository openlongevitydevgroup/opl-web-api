from rest_framework import serializers
from .models.questions import Questions, RelatedQuestions, SubmittedQuestions
# from questions.models import CurrentQuestions, SubmittedQuestions
from rest_framework_recursive.fields import RecursiveField


class RecursiveSerializer(serializers.Serializer):
    ''' Handle self-nested serializer'''

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(
            instance, context=self.context)
        return serializer.data


class QuestionSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)
 
    class Meta:
        model = Questions
        fields = ['question_id', 'title', 'description',
                  'contact', 'reference', 'parent_question', 'children']    
    def get_children(obj):
        return QuestionSerializer(obj.parent.all(), many=True).data


class SubmittedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedQuestions
        fields = ['question_id', 'title', 'description',
                  'species', 'citation', 'parent_question', 'contact']
