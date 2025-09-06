from django.contrib import admin
from .models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'updated_at', 'created_at')
    list_filter = ('category', 'is_featured', 'updated_at', 'created_at')
    search_fields = ('title', 'technologies', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('updated_at', 'created_at')

admin.site.site_header = "Moisés Portfolio Admin"
admin.site.site_title = "Moisés Portfolio Admin Portal"
admin.site.index_title = "Welcome to Moisés Portfolio Admin"

admin.site.register(Project, ProjectAdmin)
