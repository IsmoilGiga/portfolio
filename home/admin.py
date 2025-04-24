from django.contrib import admin
from home.models import Contact, Project
# Register your models here.
admin.site.register(Contact)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    list_filter = ('title',)