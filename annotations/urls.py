from django.urls import path, include
from rest_framework import routers
from annotations.views.gene_view import GeneViewSet, GeneProblemViewSet
from annotations.views.subject_view import (
    SubjectViewSet,
    SubjectProblemViewSet,
)


# Register routers the viewsets
router = routers.DefaultRouter()
router.register(r"gene", GeneViewSet, basename="genes")
router.register(f"subject", SubjectViewSet, basename="subjects")


# Create a list of prefixes for the viewsets for urls to be dynamically generated
viewsets_patterns = [
    (GeneProblemViewSet, "gene"),
    (SubjectProblemViewSet, "subject"),
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
