from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from open_problems.serializers import OPSerializer
from .models.open_problems import OpenProblems
from open_problems.serializers import SubmittedProblemSerializer as SPSerializer
from open_problems.serializers import ParentSerializer as PSerializer
from open_problems.serializers import SubmissionSerializer as SSerializer
from .models.open_problems import SubmittedProblems as SOP
from .models.submissions import ResearchSubmission, SolutionSubmission
from requests import post


@api_view(['GET'])
def questions_list(request):
    questions = OpenProblems.objects.all()
    serializer = OPSerializer(questions, many=True)
    return Response(serializer.data)

# Get the root questions


@api_view(['GET'])
def questions_root(request):
    root_questions = OpenProblems.objects.filter(parent_question=None)
    serializer = OPSerializer(root_questions, many=True)
    return Response(serializer.data)

# Returns a single question with its child questions


@api_view(['GET'])
def question_detail(request, id):
    ''' Retrieve a single question and its children'''
    question = OpenProblems.objects.get(question_id=id)
    parent_question = question.parent_question

    serializer = OPSerializer(question)

    if not parent_question:
        parent_serializer = None
    else:
        parent_serializer = PSerializer(parent_question).data

    data = {
        "open_problem": serializer.data, 
        "parent_data": parent_serializer
    }
    return Response(data)

@api_view(['GET', 'POST'])
@csrf_exempt
def submitted_questions(request):
    ''' Submit a new question '''
    if request.method == 'GET':
        questions = SOP.objects.all()
        serializer = SPSerializer(questions, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        question_serializer = SPSerializer(data=request.data)
        if question_serializer.is_valid(raise_exception=True):
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def verify_token(request):
    ''' Verify google recaptcha token'''
    if request.method == 'POST':
        data = request.data
        post_request = post('https://www.google.com/recaptcha/api/siteverify', data={'secret':data['secret'], 'response':data['response'] })
        content = post_request.text
        return Response(content)

@api_view(["POST"])    
def submit_proposal(request):
    if request.method == "POST": 
        submission_data = request.data
        submission_serializer = SSerializer(data=submission_data, context={type:""})
        type = submission_serializer.get_type()