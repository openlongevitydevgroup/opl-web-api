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

    print(type, value)
