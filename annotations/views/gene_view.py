from rest_framework.decorators import api_view
from .get_annotations import get_annotation
from annotations.models.genes import GeneProblem
from annotations.serializers.gene_serializer import GeneProblemlSerializer


# Get genes for one open problem 
@api_view(["GET"])
def get_genes(request, id): 
    return get_annotation(id, GeneProblem, GeneProblemlSerializer)

@api_view(["GET"])
def get_gene(request,id): 
    return get_annotation_details(id, Gene, GeneSerializer)

