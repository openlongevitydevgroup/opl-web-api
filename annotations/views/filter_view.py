from typing import Any, List

from django.db.models import QuerySet
from requests import Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from open_problems.models.open_problems import OpenProblems
from open_problems.serializers.OpenProblems import OpenProblemsSerializer


class FilterOpenProblemsView(APIView):
    def get_queryset(self, request: Request) -> "QuerySet[OpenProblems]":
        return OpenProblems.objects.all()

    def get(self, request: Request, *args, **kwargs):
        ...

    @staticmethod
    def filter_by_annotations(
        queryset: QuerySet, annotation_type: str, ids: list[int]
    ) -> QuerySet:
        # Quit the function if id list is empty
        if len(ids) == 0:
            return queryset
        # Filter by annotation ID
        if annotation_type == "subject":
            return queryset.filter(subjectproblem__subject__id__in=ids)
        elif annotation_type == "gene":
            return queryset.filter(geneproblem__gene__id__in=ids)
        elif annotation_type == "compound":
            return queryset.filter(compoundproblem__compound__id__in=ids)
        elif annotation_type == "species":
            return queryset.filter(speciesproblem__species__id__in=ids)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        queryset = self.get_queryset()
        filters = request.data
        for key, value in filters.items():
            if key == "sorting":
                continue
            else:
                ids: List[int] = [request_object.get("id") for request_object in value]
                queryset = self.filter_by_annotations(
                    queryset=queryset, annotation_type=key, ids=ids
                )

        serializer = OpenProblemsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
