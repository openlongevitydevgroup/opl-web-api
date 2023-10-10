from annotations.models.species import Species, SpeciesProblems
from .annotation_view import AnnotationViewSet, AnnotationProblemViewSet
from annotations.serializers.species_serializer import (
    SpeciesSerializer,
    SpeciesProblemSerializer,
)


class SpeciesViewSet(AnnotationViewSet):
    """Viewset for species model"""

    def __init__(self, *args, **kwargs):
        super().__init__(Species, SpeciesSerializer, *args, **kwargs)


class SpeciesProblemViewSet(AnnotationProblemViewSet):
    """Viewset for SpeciesProblem Model"""

    def __init__(self):
        super().__init__(
            SpeciesProblems, SpeciesProblemSerializer, annotation_foreign_key="species"
        )
