from rest_framework.decorators import api_view
from .get_annotations import get_annotation
from annotations.models.theory import TheoryProblem 
from annotations.serializers.theory_serializer import TheoryProblemSerializer

        
@api_view(["GET"])
def get_theories(request,id): 
    return get_annotation(id, TheoryProblem, TheoryProblemSerializer)