import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.get_doi_information import doi_crossref_search
from utils.get_pmid_information import get_pmid_information


@api_view(["POST"])
def verify_reference(request):
    json_request = json.loads(request.body)
    reference_type = json_request["type"]
    value = json_request["value"]

    if reference_type == "DOI":
        doi_information = doi_crossref_search(value)
        if not doi_information:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data=doi_information, status=status.HTTP_200_OK)
    elif reference_type == "PMID":
        pmid_information = get_pmid_information(value)
        if not pmid_information:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data=pmid_information, status=status.HTTP_200_OK)


@api_view(["POST"])
def verify_references(request):
    # Verify multiple references in one request
    json_request = json.loads(request.body)
    references = json_request["references"]
    verified_references = []
    unverified_references = []

    for reference in references:
        reference_type = reference["type"]
        value = reference["value"]
        if reference_type == "DOI":
            doi_information = doi_crossref_search(value)
            if not doi_information:
                unverified_references.append(
                    {"type": "DOI", "value": value, "error": "Not found"}
                )
            else:
                verified_references.append(doi_information)
        elif reference_type == "PMID":
            try:
                pmid_information = get_pmid_information(value)
                print("DONE")
            except ValueError:
                print("error")
                unverified_references.append(
                    {"type": "PMID", "value": value, "error": "Not found"}
                )
            else:
                print("no error")
                if not pmid_information:
                    unverified_references.append(
                        {"type": "PMID", "value": value, "error": "Not found"}
                    )
                else:
                    verified_references.append(pmid_information)
    return Response(
        data={
            "verified_references": verified_references,
            "unverified_references": unverified_references,
        },
        status=status.HTTP_200_OK,
    )
