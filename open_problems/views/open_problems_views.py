from django.db import models
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from open_problems.models.open_problems import OpenProblems
from open_problems.serializers.OpenProblems import (
    OpenProblemsSerializer,
)
from open_problems.serializers.serializers import ContactSerializer
from open_problems.serializers.serializers import ParentSerializer as PSerializer
from ..utils.clean_query_params import clean_query_params
from ..utils.queryset_helpers import (
    get_queryset_ordered,
    get_queryset_annotated,
)


class RetrieveProblems(ListAPIView):
    serializer_class = OpenProblemsSerializer

    @staticmethod
    def sort_queryset(queryset: QuerySet, sorting: str) -> QuerySet:
        if sorting == "latest":
            return get_queryset_ordered(
                queryset=queryset, id_string="-problem_id", is_active=True
            )
        elif sorting == "root":
            return get_queryset_ordered(
                queryset=queryset, id_string="-problem_id", is_active=True, parent=None
            )
        elif sorting == "answered":
            return get_queryset_annotated(
                queryset=queryset,
                annotate_by={"submission_count": models.Count("submission")},
                id_string="-submission_count",
                filters=[
                    {"submission__is_active": True},
                    {"submission_count__gte": 1},
                ],
            )
        elif (
            sorting == "top"
        ):  # Ordering by descendants - may not be used in the future
            return get_queryset_ordered(
                queryset=queryset, id_string="-descendants_count", is_active=True
            )
        elif sorting == "submissions":
            return get_queryset_annotated(
                queryset,
                annotate_by={"submission_count": models.Count("submission")},
                id_string="-submission_count",
            )

    @staticmethod
    def filter_by_annotations(
        queryset: QuerySet, annotation_type: str, ids: [int]
    ) -> QuerySet:
        if len(ids) == 0:
            return queryset
        else:
            filter_keyword = f"{annotation_type}problem__{annotation_type}__id__in"
            return queryset.filter(**{filter_keyword: ids})

    def get_queryset(self) -> QuerySet:
        queryset = OpenProblems.objects.all()
        query_params = clean_query_params(self.request.query_params)
        # Remove sorting and store separately as we want to sort at the end and to remove it from the annotation
        # filtering loop below.
        if "sorting" in query_params.keys():
            sorting = query_params.pop("sorting")[0]
        else:
            sorting = (
                "latest"  # Set sorting to latest as default if there is no value there
            )

        for parameter_name, parameter_value in query_params.items():
            queryset = self.filter_by_annotations(
                queryset=queryset, annotation_type=parameter_name, ids=parameter_value
            )
        queryset = self.sort_queryset(queryset, sorting)

        return queryset


# Get a singular open problems with additional information such as contact, parent problem.
@api_view(["GET"])
def open_problems_single(request, id):
    """Retrieve a single question and its children"""
    problem = OpenProblems.objects.get(problem_id=id)
    parent = problem.parent_problem
    serializer = OpenProblemsSerializer(problem)
    contact = problem.contact

    if not parent:
        parent_serializer = None
    else:
        parent_serializer = PSerializer(parent).data
    if not contact:
        contact_serializer = None
    else:
        contact_serializer = ContactSerializer(contact).data

    data = {
        "open_problem": serializer.data,
        "parent_data": parent_serializer,
        "contact": contact_serializer,
    }
    return Response(data)


class RetrieveSingleInstance(RetrieveAPIView):
    serializer_class = OpenProblemsSerializer


# Get all open problems that have been answered  (i.e. have at least one submission)
@api_view(["GET"])
def open_problems_answered(request):
    open_problems_answered = (
        OpenProblems.objects.filter(is_active=True)
        .annotate(submission_count=models.Count("submission"))
        .filter(submission__is_active=True)
        .filter(submission_count__gte=1)
        .order_by("-submission_count")  # Order by submission count in descending order
    )
    serializer = OpenProblemsSerializer(open_problems_answered, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
