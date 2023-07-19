from django.urls import path 
from annotations.views.theory_view import get_theories
urlpatterns = [
    path("<int:id>/theory", get_theories)
]