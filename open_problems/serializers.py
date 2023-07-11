from rest_framework import serializers
from .models.open_problems import OpenProblems, RelatedProblem, SubmittedProblems
from rest_framework_recursive.fields import RecursiveField


class RecursiveSerializer(serializers.Serializer):
    ''' Handle self-nested serializer'''

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(
            instance, context=self.context)
        return serializer.data

class ParentSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = OpenProblems
        fields  = ["question_id", "title"]


class OPSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True) 
    class Meta:
        model = OpenProblems
        fields = ['question_id', 'title', 'description',
                  'contact', 'reference', 'parent_question', 'children']    
    def get_children(obj):
        return OPSerializer(obj.parent.all(), many=True).data


class SubmittedProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedProblems
        fields = ['question_id', 'title', 'description',
                  'species', 'citation', 'parent_question', 'contact']

    