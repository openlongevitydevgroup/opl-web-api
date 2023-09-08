import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from open_problems.serializers.serializers import (
    SubmittedProblems,
    SubmittedProblemSerializer,
)
from utils.get_doi_information import doi_crossref_search
from utils.get_pmid_information import get_pmid_citation


class SubmitOpenProblem(APIView):
    def convert_references(self, request):
        references = request.data.get("references")
        references_json = json.loads(references)

        references_dict = {}

        for ref, key in references_json.items():
            type = key["type"]
            value = key["value"]
            if type == "DOI":
                citation_information = doi_crossref_search(value)
                references_dict[ref] = citation_information
            elif type == "PMID":
                citation_information = get_pmid_citation(value)
                references_dict[ref] = citation_information
        return references_dict

    def post(self, request, *args, **kwargs):
        # First convert the references - they should have already been verified by the api and client before submission
        if request.data.get("references"):
            references = self.convert_references(request)
            data = request.data
            data["references"] = json.dumps(
                references
            )  # Replace the references with the converted references
        else:
            data = request.data
        problem_serializer = SubmittedProblemSerializer(data=data)
        if problem_serializer.is_valid(raise_exception=True):
            problem_serializer.save()
            return Response(problem_serializer.data, status=status.HTTP_201_CREATED)
