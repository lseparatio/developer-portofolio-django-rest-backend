from django.contrib import admin
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'project_name',
        'project_description',
        'project_image',
        'project_icon',
        'project_live_link',
        'project_github_link',
        'project_start_date',
        'html',
        'css',
        'bootstrap',
        'javascript',
        'python',
        'flask',
        'django',
        'sql',
        'mongodb',
        'postgres',
        'deployment_required',
        'shared_hosting',
        'vps',
        'email_server_setup',
    )


admin.site.register(Projects, ProjectsAdmin)
