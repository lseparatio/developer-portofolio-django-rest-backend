from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Projects
        fields = [
            'id', 'user', 'project_name', 'project_description', 'project_image', 'project_icon',
            'project_github_link', 'project_start_date', 'project_end_date', 'html', 'css', 'bootstrap', 'javascript',
            'python', 'flask', 'django', 'sql', 'mongodb', 'postgres', 'deployment_required', 'shared_hosting', 'vps', 'email_server_setup',
            'is_user',
        ]
