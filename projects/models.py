from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(
        max_length=254, default='Please provide a project title')
    project_description = models.CharField(
        max_length=500, default='Please provide a project description')
    project_image = models.ImageField(
        upload_to='images/', default='../media/img-commig-soon.webp')
    project_icon = models.ImageField(blank=True, null=True)
    project_live_link = models.URLField(max_length=265, null=True, blank=True)
    project_github_link = models.URLField(
        max_length=265, blank=True, null=True)
    project_start_date = models.DateField(null=True, blank=True)
    project_end_date = models.DateField(null=True, blank=True)
    html = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    bootstrap = models.BooleanField(default=False)
    materialize = models.BooleanField(default=False)
    javascript = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    flask = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    reactJS = models.BooleanField(default=False)
    use_database = models.BooleanField(default=False)
    sql = models.BooleanField(default=False)
    mongodb = models.BooleanField(default=False)
    postgres = models.BooleanField(default=False)
    deployment_required = models.BooleanField(default=False)
    is_deployed = models.BooleanField(default=False)
    shared_hosting = models.BooleanField(default=False)
    heroku = models.BooleanField(default=False)
    aws = models.BooleanField(default=False)
    vps = models.BooleanField(default=False)
    email_server_setup = models.BooleanField(default=False)
    stripe = models.BooleanField(default=False)
    paypal = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name
