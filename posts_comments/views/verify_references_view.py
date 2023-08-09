from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from utils.get_pmid_information import get_pmid_information
from utils.get_doi_information import doi_crossref_search
import json


@api_view(["POST"])
def verify_reference(request, reference):
    json_request = json.loads(request.body)

    type = json_request["type"]
    value = json_request["value"]
    if type == "DOI":
        doi_information = doi_crossref_search(value)
        if not doi_information:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data=doi_information, status=status.HTTP_200_OK)
    elif type == "PMID":
        pmid_information = get_pmid_information(value)
        if not pmid_information:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data=pmid_information, status=status.HTTP_404_NOT_FOUND)
