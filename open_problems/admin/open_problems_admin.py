from django.contrib import admin
from open_problems.models.open_problems import OpenProblems, RelatedProblem
from open_problems.forms.forms import CreateRelationForm
from django.shortcuts import render, redirect


def set_answers(request, queryset):
    parent_id = request.POST.get('parent_problem')
    parent_query = queryset.get(question_id=parent_id)
    child_query = queryset.all().exclude(question_id=parent_id)[0]
    print(parent_query)
    return parent_query, child_query


class OPAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OpenProblems._meta.get_fields()]
    actions = ['create_relationship']
    search_fields = ['problem_id', 'title']

    @admin.action(description="Create a relationship between two questions")
    def create_relationship(self, request, queryset):
        query1, query2 = queryset[0:2]
        data = [(query1.problem_id, query1.title), (query2.problem_id, query2.title)]
        form = CreateRelationForm(data=data)
        form_html = form.as_table()
        if 'apply' in request.POST:
            parent, child = set_answers(request, queryset)
            RelatedProblem(parent_id=parent, child_id=child).save()
            self.message_user(request, f'Created relationship between: {parent.title} and {child.title}')
            return redirect('admin:questions_questions_changelist')

        else:
            return render(request, 'admin/create_relation.html', context={'form': form_html, 'query': queryset})


admin.site.register(OpenProblems, OPAdmin)
