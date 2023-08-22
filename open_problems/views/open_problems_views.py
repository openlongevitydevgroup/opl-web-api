from rest_framework import status
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from open_problems.serializers.OpenProblems import OpenProblemsSerializer
from open_problems.models.open_problems import OpenProblems
from open_problems.serializers.serializers import ParentSerializer as PSerializer
from open_problems.serializers.serializers import ContactSerializer
from open_problems.serializers.OpenProblems import DescendantsDescendingSerializer


# get open problems by oldest -> newest
@api_view(['GET'])
def open_problems_latest(request):
    questions = OpenProblems.objects.filter(is_active=True).order_by("problem_id")
    serializer = OpenProblemsSerializer(questions, many=True)
    return Response(serializer.data)


# get open problems by oldest -> newest for root problems only
@api_view(["GET"])
def open_problems_root_latest(request):
    root_problems = OpenProblems.objects.filter(parent_problem=None, is_active=True).order_by("problem_id")
    serializer = OpenProblemsSerializer(root_problems, many=True)
    return Response(serializer.data)


# Get a singular open problems with additional information such as contact, parent problem.
@api_view(["GET"])
def open_problems_single(request, id):
    """ Retrieve a single question and its children"""
    problem = OpenProblems.objects.get(problem_id=id)
    parent = problem.parent_problem
    serializer = OpenProblemsSerializer(problem)
    contact = problem.contact

    if not parent:
        parent_serializer = None
    else:
        parent_serializer = PSerializer(parent).data
    if not contact:
        contact_serializer = None
    else:
        contact_serializer = ContactSerializer(contact).data

    data = {
        "open_problem": serializer.data,
        "parent_data": parent_serializer,
        "contact": contact_serializer
    }
    return Response(data)


# Get open problems sorted by number of descendants in descending order.
@api_view(["GET"])
def open_problems_descendants_descending(request):
    all_problems = OpenProblems.objects.filter(is_active=True).order_by("-descendants_count")
    serializer = DescendantsDescendingSerializer(all_problems, many=True)
    return Response(serializer.data)

# Get open problems sorted by the number of submitted solutions in descending order.
@api_view(["GET"])
def open_problems_submissions_descending(request):
    open_problems_sorted = OpenProblems.objects.filter(is_active=True).annotate(submission_count=models.Count("submission")).order_by("-submission_count")
    serializer = OpenProblemsSerializer(open_problems_sorted, many=True)
    return Response(serializer.data,status=404)

