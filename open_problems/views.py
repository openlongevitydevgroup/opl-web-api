from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from open_problems.serializers import OPSerializer
from .models.open_problems import OpenProblems
from .models.open_problems import ProblemReference
from open_problems.serializers import SubmittedProblemSerializer as SPSerializer
from open_problems.serializers import ParentSerializer as PSerializer
from .models.open_problems import SubmittedProblems as SOP
from open_problems.serializers import ContactSerializer
from open_problems.serializers import FilterReferenceSerializer
from requests import post


@api_view(['GET'])
def questions_list(request):
    questions = OpenProblems.objects.all().order_by("problem_id")
    serializer = OPSerializer(questions, many=True)
    return Response(serializer.data)

# Get the root questions


@api_view(['GET'])
def questions_root(request):
    root_questions = OpenProblems.objects.filter(parent_problem=None).order_by("problem_id")
    serializer = OPSerializer(root_questions, many=True)
    return Response(serializer.data)

# Returns a single question with its child questions


@api_view(['GET'])
def question_detail(request, id):
    ''' Retrieve a single question and its children'''
    problem = OpenProblems.objects.get(problem_id=id)
    parent = problem.parent_problem
    serializer = OPSerializer(problem)
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

@api_view(['GET', 'POST'])
def submitted_questions(request):
    ''' Submit a new question '''
    if request.method == 'GET':
        problems = SOP.objects.all()
        serializer = SPSerializer(problems, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        problem_serializer = SPSerializer(data=request.data)
        if problem_serializer.is_valid(raise_exception=True):
            problem_serializer.save()
            return Response(problem_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def verify_token(request):
    ''' Verify google recaptcha token'''
    if request.method == 'POST':
        data = request.data
        post_request = post('https://www.google.com/recaptcha/api/siteverify', data={'secret':data['secret'], 'response':data['response'] })
        content = post_request.text
        return Response(content)

# Get references for an open problem
@api_view(['GET'])
def get_references(request,id): 
    references = ProblemReference.objects.filter(problem_id=id)

    if not references: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    else: 
        serializer = FilterReferenceSerializer(references, many=True)
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
