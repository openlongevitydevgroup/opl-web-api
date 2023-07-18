from rest_framework import serializers
from .models.open_problems import OpenProblems, RelatedProblem, SubmittedProblems, Contact, ProblemReference
from .models.references import Reference

# Serializer to retrieve children of parent node
class RecursiveSerializer(serializers.Serializer):
    ''' Handle self-nested serializer'''
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(
            instance, context=self.context)
        return serializer.data
# Serializer for parent node of open problem
class ParentSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = OpenProblems
        fields  = ["problem_id", "title"]

class ContactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Contact
        fields = ["first_name", "last_name"]

# Serializer for reviewed open problems
class OPSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True) 
    class Meta:
        model = OpenProblems
        fields = ['problem_id', 'title', 'description',
                  'contact', 'parent_problem', 'children']    
    def get_children(obj):
        return OPSerializer(obj.parent.all(), many=True).data

# Serializer for user submitted open problems
class SubmittedProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedProblems
        fields = ['problem_id', 'title', 'description',
                  'species', 'citation', 'parent_problem', 'contact']


# Serializer to return a reference to be nested in serializer below 
class ReferenceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Reference
        fields = "__all__"

# For all references for a particular open problem
class FilterReferenceSerializer(serializers.ModelSerializer): 
    reference = ReferenceSerializer(source="reference_id")
    class Meta: 
        model = ProblemReference
        fields = ["reference"]
