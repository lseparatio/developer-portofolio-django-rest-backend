from django.contrib import admin
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'project_name',
        'project_description',
        'project_image',
        'project_icon',
        'project_github_link',
        'project_start_date',
        'project_end_date',
        'html',
        'css',
        'bootstrap',
        'materialize',
        'javascript',
        'python',
        'flask',
        'django',
        'reactJS',
        'use_database',
        'sql',
        'mongodb',
        'postgres',
        'deployment_required',
        'is_deployed',
        'shared_hosting',
        'heroku',
        'aws',
        'vps',
        'email_server_setup',
    )


admin.site.register(Projects, ProjectsAdmin)
