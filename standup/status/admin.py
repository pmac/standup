from django.contrib import admin

from standup.status.models import Project, Team


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = (('name', 'slug'), 'color', 'repo_url')
    list_display = ['name', 'color']
    list_editable = ['color']
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'repo_url']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}
