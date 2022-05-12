from django.conf import settings
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    author_user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="Contributor")


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributors")
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    #    permission = models.CharField(max_length=128)
    role = models.CharField(max_length=128)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=128)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authors')
    assignee_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignees')
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=128)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
