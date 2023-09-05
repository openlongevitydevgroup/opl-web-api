from django.contrib import admin

from open_problems.models.open_problems import OpenProblems, SubmittedProblems


class SubmittedProblemsAdmin(admin.ModelAdmin):
    display = [field.name for field in SubmittedProblems._meta.get_fields()]
    actions = ["move_to_open_problems"]

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
