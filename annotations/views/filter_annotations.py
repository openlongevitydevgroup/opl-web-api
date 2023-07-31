from open_problems.models.open_problems import OpenProblems
from annotations.models.theory import Theory
def filter_by_annotations(annotations):
    query_set = OpenProblems.objects.all() 
    for annotation_name, annotation_value in annotations.items():
        try:
            # Retrieve the model dynamically based on the annotation name
            annotation_model = globals()[annotation_name]
            # Check if the model name is the same as the annotation name
            if annotation_model.__name__ == annotation_name:
                # Use the correct related name for the filtering (assuming 'theoryproblem__theory')
                related_name = f"{annotation_name.lower()}problem__{annotation_name.lower()}"
                query_set = query_set.filter(**{f"{related_name}__pk": annotation_value})
                return query_set

        except KeyError:
            return KeyError
