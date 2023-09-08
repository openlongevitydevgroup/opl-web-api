import json

from rest_framework import serializers

from utils.get_doi_information import doi_crossref_search
from utils.get_pmid_information import get_pmid_citation
from utils.recursive_serializer import RecursiveSerializer

from ..models.open_problems import (
    Contact,
    OpenProblems,
    ProblemReference,
    SubmittedProblems,
)
from ..models.references import Reference


# Serializer for parent node of open problem
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenProblems
        fields = ["problem_id", "title"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name"]


# Serializer for reviewed open problems
class OpenProblemsSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = OpenProblems
        fields = [
            "problem_id",
            "title",
            "description",
            "contact",
            "parent_problem",
            "descendants_count",
            "children",
        ]


# Serializer for user submitted open problems
class SubmittedProblemSerializer(serializers.ModelSerializer):
    # converted_references = serializers.SerializerMethodField()

    class Meta:
        model = SubmittedProblems
        fields = [
            "problem_id",
            "title",
            "description",
            "species",
            "references",
            "parent_problem",
            "contact",
        ]

    # def get_converted_references(self, instance):
    #     references = instance.references
    #     reference_json = json.loads(references)
    #     print(reference_json)
    #     reference_dict = {}

    #     for key, ref in reference_json.items():
    #         if ref["type"] == "DOI":
    #             reference_dict[ref["value"]] = doi_crossref_search(ref["value"])
    #         elif ref["type"] == "PMID":
    #             reference_dict[ref["value"]] = get_pmid_citation(ref["value"])
    #     instance.references = json.dumps(reference_dict)
    #     return reference_dict

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     return data


# Serializer to return a reference to be nested in serializer below
class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = "__all__"


# For all references for a particular open problem
class FilterReferenceSerializer(serializers.ModelSerializer):
    reference = ReferenceSerializer(source="reference_id")

    class Meta:
        model = ProblemReference
        fields = ["reference"]
