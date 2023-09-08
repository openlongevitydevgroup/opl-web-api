from django.contrib import admin

from open_problems.models.open_problems import OpenProblems, SubmittedProblems
from open_problems.serializers.serializers import SubmittedProblemSerializer


class SubmittedProblemsAdmin(admin.ModelAdmin):
    display = [field.name for field in SubmittedProblems._meta.get_fields()] + [
        "converted_references"
    ]
    actions = ["move_to_open_problems"]

    def get_converted_references(self, obj):
        serializer = SubmittedProblemSerializer(instance=obj)
        return serializer.data["converted_references"]

    get_converted_references.short_description = "Converted References"

    @admin.action(
        description="Move submitted problem(s) to the official list of open problems"
    )
    def move_to_open_problems(self, request, queryset):
        for submitted_problem in queryset:
            open_problem = OpenProblems.objects.create(
                title=submitted_problem.title,
                description=submitted_problem.description,
                parent_problem=submitted_problem.parent_problem,
            )
            open_problem.save()

        queryset.delete()
