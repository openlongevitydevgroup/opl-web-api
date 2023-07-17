from rest_framework import serializers
from .models.open_problems import OpenProblems, RelatedProblem, SubmittedProblems, Contact
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
        fields  = ["problem_id", "title"]

class ContactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Contact
        fields = ["first_name", "last_name"]


class OPSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True) 
    class Meta:
        model = OpenProblems
        fields = ['problem_id', 'title', 'description',
                  'contact', 'parent_problem', 'children']    
    def get_children(obj):
        return OPSerializer(obj.parent.all(), many=True).data


class SubmittedProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedProblems
        fields = ['problem_id', 'title', 'description',
                  'species', 'citation', 'parent_problem', 'contact']


