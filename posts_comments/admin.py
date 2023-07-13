from django.contrib import admin
from .models.submissions import * 
from .models.comments import *
# Register your models here.


admin.site.register(Submission)
admin.site.register(SubmittedReferences)