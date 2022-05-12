from django.conf import settings
from django.db import models


class Project(models.Model):
    TYPE_CHOICES = (
        ("FRONTEND", "Front-end"),
        ("BACKEND", "Back-end"),
        ("IOS", "iOS"),
        ("ANDROID", "Android"),
    )
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    author_user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, through="Contributor")


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributors")
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    # permission = models.CharField(max_length=128)
    role = models.CharField(max_length=128)


class Issue(models.Model):
    TAG_CHOICES = (
        ("BUG", "Bug"),
        ("IMPROVEMENT", "Improvement"),
        ("TASK", "Task"),
    )
    PRIORITY_CHOICES = (
        ("HIGH", "High"),
        ("MEDIUM", "Medium"),
        ("LOW", "Low"),
    )
    STATUS_CHOICES = (
        ("TODO", "To Do"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
    )
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    tag = models.CharField(max_length=16, choices=TAG_CHOICES)
    priority = models.CharField(max_length=16, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authors')
    assignee_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignees',
                                      default=author_user)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=128)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
