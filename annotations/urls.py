from django.urls import path, include
from rest_framework import routers
from annotations.views.gene_view import GeneViewSet, GeneProblemViewSet
from annotations.views.theory_view import (
    TheoryViewSet,
    TheoryProblemViewSet,
)


# Register routers the viewsets
router = routers.DefaultRouter()
router.register(r"genes", GeneViewSet, basename="genes")
router.register(f"theories", TheoryViewSet, basename="theories")


# Create a list of prefixes for the viewsets for urls to be dynamically generated
viewsets_patterns = [
    (GeneProblemViewSet, "genes"),
    (TheoryProblemViewSet, "theories"),
]


# Base url api/annotations/
urlpatterns = [path("", include(router.urls))]


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
