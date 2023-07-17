from django.urls import path 
from annotations.views.theory_view import theory_annotation 
urlpatterns = [
    path("<int:id>/theory", theory_annotation)
]