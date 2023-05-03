from rest_framework import serializers
from questions.models import Question, SubmittedQuestions 
from rest_framework_recursive.fields import RecursiveField 

class QuestionSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    class Meta:
        model = Question
        fields = ['question_id', 'title', 'excerpt', 'content', 'species', 'citation', 'parent_question', 'children']

    def create(self, validated_data):
        return Question.objects.create(**validated_data)
    

class SubmittedQuestionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SubmittedQuestions
        fields = ['question_id', 'title', 'excerpt', 'content', 'species', 'citation', 'parent_question']

