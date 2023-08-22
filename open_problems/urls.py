from django.urls import path
from .views.open_problems_views import open_problems_latest, open_problems_root_latest, \
    open_problems_descendants_descending, open_problems_single, open_problems_submissions_descending
from .views.submitted_problems_views import submitted
from .views.utils import verify_token
from .views.references_views import get_references

urlpatterns = [
    # All problems from latest -> oldest. Default
    path('', open_problems_latest),
    # All root problems from latest -> oldest.
    path('root', open_problems_root_latest),
    # All open problems from most descendants -> least
    path("sorted/descendants", open_problems_descendants_descending),
    # All open problems from most solutions -> least
    path("sorted/submissions", open_problems_submissions_descending),
    path('<int:id>', open_problems_single),
    path('submit', submitted),
    path('verify-token', verify_token),
    path("<int:id>/references", get_references)
]
