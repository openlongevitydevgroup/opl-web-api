from rest_framework.decorators import api_view
from .get_annotations import get_annotation, get_annotation_details
from annotations.models.theory import TheoryProblem, Theory
from annotations.serializers.theory_serializer import (
    TheoryProblemSerializer,
    TheorySerializer,
)


@api_view(["GET"])
def get_theories(request, id):
    return get_annotation(id, TheoryProblem, TheoryProblemSerializer)


@api_view(["GET"])
def get_theory(request, id):
    return get_annotation_details(id, Theory, TheorySerializer)
