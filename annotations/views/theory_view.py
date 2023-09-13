from rest_framework.decorators import api_view
from .annotation_viewset import AnnotationViewSet, AnnotationProblemViewSet
from annotations.models.theory import Theory, TheoryProblem
from annotations.serializers.theory_serializer import (
    TheoryProblemSerializer,
    TheorySerializer,
)


class TheoryViewSet(AnnotationViewSet):
    """Viewset for Theory model"""

    def __init__(self, *args, **kwargs):
        super().__init__(
            Theory,
            TheorySerializer,
        )


class TheoryProblemViewSet(AnnotationProblemViewSet):
    """Viewset for TheoryProblem model"""

    def __init__(self, *args, **kwargs):
        super().__init__(
            TheoryProblem, TheoryProblemSerializer, annotation_foreign_key="theory_id"
        )
