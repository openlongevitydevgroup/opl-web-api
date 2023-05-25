from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework.parsers import JSONParser
from questions.serializers import QuestionSerializer as QS
from questions.serializers import SubmittedQuestionSerializer as SQSerializer
from questions.serializers import QuestionRecursiveSerializer as QRSerializer
from questions.models import CurrentQuestions
from  questions.models import SubmittedQuestions as SQ

# Create your views here.
@api_view(['GET', 'POST'])
def questions_lists(request): 
    if request.method == 'GET': 
        questions = CurrentQuestions.objects.all()
        serializer = QS(questions, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        data = JSONParser.parse(request.data)
        serializer = QS(data = data)
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def question_detail_single(request, id):
    ''' Retrieve, edit, put single question '''
    try: 
        question = CurrentQuestions.objects.get(question_id = id)
    except CurrentQuestions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        question_serializer = QS(question)
        return Response(question_serializer.data)
    elif request.method == 'PUT': 
        question_serializer = QS(question, data = request.data)
        if question_serializer.is_valid(): 
            question_serializer.save() 
            return Response(question_serializer.data)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE': 
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def submitted_questions(request):
    ''' Submit a new question '''
    if request.method =='GET': 
        questions = SQ.objects.all()
        serializer = SQSerializer(questions, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        question_serializer = SQSerializer(data=request.data)
        if question_serializer.is_valid(raise_exception=True): 
            question_serializer.save()
            return Response(question_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def recursive_questions(request): 
    query = CurrentQuestions.objects.filter(parent_question__isnull=True)
    if request.method == 'GET': 
        serializer = QRSerializer(query, many=True)
        return Response(serializer.data)







