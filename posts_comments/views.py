from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models.submissions import Submission
from .models.submissions import SubmissionReferences
from .serializers.submissions_serializer import SubmissionSerializer
from .serializers.submissions_serializer import SubmissionReferences
from open_problems.models import OpenProblems
# Create your views here.
# Getting the user submitted posts for a single open problem
@api_view(["GET"])
def get_posts(requests,id): 
    submissions_for_open_problem = Submission.objects.filter(open_problem=id)
    serializer = SubmissionSerializer(submissions_for_open_problem, many=True)
    reviewed_references = SubmissionReferences.objects.filter()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(["POST"])
def submit_post(request, id):
    if request.method == "POST": 
        serializer = SubmissionSerializer(data=request.data)
        open_problem = OpenProblems.objects.filter(question_id = id ).exists()
        if serializer.is_valid(raise_exception=True) & open_problem:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
