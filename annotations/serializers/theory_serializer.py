from rest_framework import serializers
from annotations.models.theory import Theory, TheoryProblem 

class TheorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Theory
        fields = ["theory_title", "theory_description", "theory_id"]

class TheoryProblemSerializer(serializers.ModelSerializer): 
    theory = TheorySerializer() 
    class Meta: 
        model = TheoryProblem
        fields = "__all__"
