from django.urls import path 
from annotations.views.theory_view import get_theories
from annotations.views.gene_view import get_genes
from annotations.views.filter_annotations_view import filter_annotations


# Base url api/annotations/filter
urlpatterns = [
    path("<int:id>/theory", get_theories), 
    path("<int:id>/genes", get_genes),
    path("filter/", filter_annotations)
]

