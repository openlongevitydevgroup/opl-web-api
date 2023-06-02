from .models.questions import Questions, SubmittedQuestions, RelatedQuestions
from .models.references import Reference, Author, Journal, RefType
from .forms.forms import CreateRelationForm
from django.contrib import admin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect



# Register your models here.
# admin.site.register(Questions)
def set_answers(request, queryset): 
    parent_id = request.POST.get('parent_question')
    parent_query = queryset.get(question_id=parent_id)
    child_query = queryset.all().exclude(question_id=parent_id)[0]
    print(parent_query)
    return parent_query, child_query


class QuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Questions._meta.fields]
    actions = ['create_relationship']
    search_fields = ['question_id', 'title']
    @admin.action(description="Create a relationship between two questions")
    def create_relationship(self, request, queryset):
        query1, query2 = queryset[0:2]
        data = [(query1.question_id, query1.title), (query2.question_id, query2.title)]
        form = CreateRelationForm(data=data)
        form_html = form.as_table()
        if 'apply' in request.POST:
            parent, child = set_answers(request, queryset)
            RQ = RelatedQuestions(parent_id=parent, child_id=child).save()
            self.message_user(request, f'Created relationship between: {parent.title} and {child.title}')
            return redirect('admin:questions_questions_changelist')

        else: 
            return render(request, 'admin/create_relation.html', context={'form': form_html, 'query':queryset})


        

admin.site.register(Questions,QuestionsAdmin)
admin.site.register(SubmittedQuestions)
admin.site.register(RelatedQuestions)
admin.site.register(Reference)
admin.site.register(Journal)
admin.site.register(RefType)

