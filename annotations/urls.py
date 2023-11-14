from django.urls import path, include
from rest_framework import routers

from annotations.views.compounds_view import CompoundViewSet, CompoundProblemViewSet
from annotations.views.gene_view import GeneViewSet, GeneProblemViewSet
from annotations.views.species_view import SpeciesViewSet, SpeciesProblemViewSet
from annotations.views.subject_view import (
    SubjectViewSet,
    SubjectProblemViewSet,
)

# Register routers the viewsets

router = routers.DefaultRouter()
viewsets = {
    "gene": GeneViewSet,
    "subject": SubjectViewSet,
    "species": SpeciesViewSet,
    "compound": CompoundViewSet,
}

for route, viewset in viewsets.items():
    router.register(route, viewset, basename=route)

# Create a list of prefixes for the viewsets for urls to be dynamically generated


viewsets_patterns = [
    (GeneProblemViewSet, "gene"),
    (SubjectProblemViewSet, "subject"),
    (SpeciesProblemViewSet, "species"),
    (CompoundProblemViewSet, "compound"),
]


# Base url api/annotations/
urlpatterns = [
    path("", include(router.urls)),
]


# Add to the urlpatterns list
for viewset, prefix in viewsets_patterns:
    urlpatterns += [
        path(
            f"{prefix}/filter/by-problem:<int:problem_id>",
            viewset.as_view({"get": "get_annotations"}),
        ),
        path(
            f"{prefix}/filter/by-annotation:<int:annotation_id>",
            viewset.as_view({"get": "get_problems"}),
        ),
    ]
