from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
      fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['created_at','url','image','media_type','owner'],'classes': ['collapse']}),
    ]
      list_filter = ['created_at']
      search_fields = ['name']  	
      list_display = ('name', 'created_at') 
admin.site.register(Card, CardAdmin)
