from django.contrib import admin
from projects.models import Project, Issue, Sprint


class IssueAdmin(admin.StackedInline):
    model = Issue


class SprintAdmin(admin.ModelAdmin):
    inlines = (IssueAdmin, )


admin.site.register(Project)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Issue)
