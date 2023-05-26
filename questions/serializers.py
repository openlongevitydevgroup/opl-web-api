from rest_framework import serializers
from .models.questions import Questions
# from questions.models import CurrentQuestions, SubmittedQuestions 
from rest_framework_recursive.fields import RecursiveField 

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['question_id', 'title', 'description', 'contact', 'species', 'reference']


    def create(self, validated_data):
        return Questions.objects.create(**validated_data)
    

# class SubmittedQuestionSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = SubmittedQuestions
#         fields = ['question_id', 'title', 'excerpt', 'species', 'citation', 'parent_question']


# class QuestionRecursiveSerializer(serializers.ModelSerializer):
#     children  = RecursiveField(many = True)
#     class Meta:
#         model = CurrentQuestions 
#         fields = ['question_id', 'title', 'excerpt', 'species', 'citation', 'parent_question', 'children']
