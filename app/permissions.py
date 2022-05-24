from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from app.models import Contributor, Project, Issue, Comment


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            if isinstance(obj, Contributor):
                contributors = Contributor.objects.filter(project__id=obj.project_id)
                return contributors.filter(user_id=request.user.pk).exists()
            if isinstance(obj, Project):
                contributors = Contributor.objects.filter(project__id=obj.pk)
                return contributors.filter(user_id=request.user.pk).exists()
            if isinstance(obj, Issue):
                print(obj.project_id)
                contributors = Contributor.objects.filter(project__id=obj.project_id)
                return contributors.filter(user_id=request.user.pk).exists()
            if isinstance(obj, Comment):
                issue = get_object_or_404(Issue, id=obj.issue_id)
                contributors = Contributor.objects.filter(project__id=issue.project_id)
                return contributors.filter(user_id=request.user.pk).exists()
        if isinstance(obj, Contributor):
            author = Contributor.objects.filter(project__id=obj.project_id).filter(role="author")
            return author.filter(user_id=request.user.pk).exists()
        if isinstance(obj, Project):
            author = Contributor.objects.filter(project__id=obj.pk).filter(role="author")
            return author.filter(user_id=request.user.pk).exists()
        if isinstance(obj, Issue):
            return obj.author == request.user
        if isinstance(obj, Comment):
            return obj.author == request.user
        return obj.user == request.user
