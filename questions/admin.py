from questions.models import * 

from django.contrib import admin

# Register your models here.
admin.site.register(Question)
admin.site.register(Species)
admin.site.register(Citation)
admin.site.register(SubmittedQuestions)