from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.submissions import Submission, SubmittedReferences, SubmissionReferences
from ..serializers.submissions_serializer import SubmissionSerializer
from ..serializers.submissions_serializer import SubmittedReferencesSerializer, SubmissionReferencesSerializer
from open_problems.models import OpenProblems
from ..utils.parse_submitted_references import parse_submitted_references

#base url  /api/posts

# Create your views here.
# Getting the user submitted posts for a single open problem

@api_view(["GET"])
def get_posts(requests, id):  # Get all posts for a given open problem problem
    submissions_for_open_problem = Submission.objects.filter(open_problem=id, is_active=True)
    serializer = SubmissionSerializer(submissions_for_open_problem, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(["GET"])  # Retrive the number of posts for a given open problem
def get_posts_counts(request, id):
    submissions_for_open_problem = Submission.objects.filter(open_problem=id, is_active=True).count()
    return Response({"post_counts": submissions_for_open_problem})


@api_view(["GET"])
def get_post(request, id):  # Return single post
    submission = Submission.objects.get(submission_id=id)
    sub_serializer = SubmissionSerializer(submission)

    # Check for submitted references:
    references = SubmittedReferences.objects.filter(submission_id=id)
    ref_serializer = SubmittedReferencesSerializer(references, many=True)
    return Response({
        "post": sub_serializer.data,
        "references": ref_serializer.data
    })


@api_view(["POST"])
def submit_post(request, id):  # Submit post for a open problem.
    if request.method == "POST":
        serializer = SubmissionSerializer(data=request.data)
        open_problem = OpenProblems.objects.filter(problem_id=id).exists()

        if serializer.is_valid(raise_exception=True) & open_problem:
            serializer.save()
            # After saving parse the submitted serializer 
            reference_data = request.data["submitted_references"]
            if reference_data:
                submission_id = serializer["submission_id"].value
                reference_list = parse_submitted_references(reference_data, submission_id)
                submitted_references_serializer = SubmittedReferencesSerializer(data=reference_list, many=True)
                if submitted_references_serializer.is_valid():
                    submitted_references_serializer.save()
                else:
                    print(submitted_references_serializer.errors)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def get_references(request, id):
    """Get references for a particular solution submission"""
    references = SubmissionReferences.objects.filter(submission_id=id)
    if references:
        serializer = SubmissionReferencesSerializer(references, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
