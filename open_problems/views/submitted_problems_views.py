from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from open_problems.serializers.serializers import SubmittedProblems
from open_problems.serializers.serializers import SubmittedProblemSerializer


@api_view(['GET', 'POST'])
def submitted(request):
    """ Submit a new question """
    if request.method == 'GET':
        submitted_problems = SubmittedProblems.objects.all()
        serializer = SubmittedProblemSerializer(submitted_problems, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        problem_serializer = SubmittedProblemSerializer(data=request.data)
        if problem_serializer.is_valid(raise_exception=True):
            problem_serializer.save()
            return Response(problem_serializer.data, status=status.HTTP_201_CREATED)
