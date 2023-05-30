from .models.questions import Questions, SubmittedQuestions, RelatedQuestions
from .models.references import Reference, Author, Journal, RefType
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse



# Register your models here.
# admin.site.register(Questions)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Questions._meta.fields]
    actions = ['create_relationship']
    @admin.action(description="Create a relationship between two questions")
    def create_relationship(self, request, queryset):
        first_two_queries = queryset[0:2]
        if 'apply' in request.method == 'POST':
            id = request.POST.get('parent')

            other_id = first_two_queries.exclude(question_id= id)
            RelatedQuestions.objects.create(parent_id=id, child_id=other_id )

        return render(request,'admin/create_relation.html', context={'queries': first_two_queries, 'action_checkbox_name':'_selected_action'})
        

admin.site.register(Questions,QuestionsAdmin)
admin.site.register(SubmittedQuestions)
admin.site.register(RelatedQuestions)
admin.site.register(Reference)
admin.site.register(Journal)
admin.site.register(RefType)

