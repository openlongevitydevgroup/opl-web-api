from django.shortcuts import render
from rest_framework.decorators import api_view
from annotations.models.theory import Theory, TheoryProblem
from annotations.serializers.theory_serializer import TheoryProblemSerializer
from open_problems.models.open_problems import OpenProblems
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view(["GET"])
def theory_annotation(request, id):
    open_problem = OpenProblems.objects.get(problem_id=id)
    if open_problem: 
        attached_theories = TheoryProblem.objects.filter(open_problem=id)
        print(attached_theories)
        if attached_theories: 
            theory_serializer = TheoryProblemSerializer(attached_theories, many=True) 
            print(theory_serializer.data)
            return Response(theory_serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(status.HTTP_204_NO_CONTENT)
        
        
     
