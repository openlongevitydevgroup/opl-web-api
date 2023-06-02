from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from questions.serializers import QuestionSerializer
from .models.questions import Questions, RelatedQuestions
from questions.serializers import SubmittedQuestionSerializer as SQSerializer
# from questions.models import CurrentQuestions
from .models.questions import SubmittedQuestions as SQ

# # Gets all the questions


@api_view(['GET'])
def questions_list(request):
    questions = Questions.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

# Get the root questions


@api_view(['GET'])
def questions_root(request):
    root_questions = Questions.objects.filter(parent_question=None)
    serializer = QuestionSerializer(root_questions, many=True)
    return Response(serializer.data)

# Returns a single question with its child questions


@api_view(['GET'])
def question_detail(request, id):
    ''' Retrieve a single question and its children'''
    question = Questions.objects.get(question_id=id)
    serializer = QuestionSerializer(question)

    return Response(serializer.data)

@api_view(['GET', 'POST'])
@csrf_exempt
def submitted_questions(request):
    ''' Submit a new question '''
    if request.method == 'GET':
        questions = SQ.objects.all()
        serializer = SQSerializer(questions, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        question_serializer = SQSerializer(data=request.data)
        if question_serializer.is_valid(raise_exception=True):
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)
