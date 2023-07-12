from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from models.submissions import Submission
from serializers.submissions_serializer import SubmissionSerializer
# Create your views here.

# Getting the user submitted posts for a single open problem
@api_view(["GET"])
def get_posts(requests,id): 
    submissions_for_open_problem = Submission.objects.filter(open_problem=id)
    serializer = SubmissionSerializer(submissions_for_open_problem, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    