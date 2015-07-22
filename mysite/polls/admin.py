from django.contrib import admin
from .models import Question
from .models import Choise
class ChoiseInline(admin.StackedInline):
    model = Choise
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
      fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
      list_filter = ['pub_date']
      search_fields = ['question_text']  	
      inlines = [ChoiseInline]   
      list_display = ('question_text', 'pub_date','was_published_recently') 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choise)