from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from app.models import Contributor, Project


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in SAFE_METHODS:
            if type(obj) == Contributor:
                return Contributor.objects \
                    .filter(project__id=obj.project_id) \
                    .filter(user_id=request.user.pk).exists()
            if type(obj) == Project:
                return Contributor.objects \
                    .filter(project__id=obj.pk) \
                    .filter(user_id=request.user.pk).exists()
        if type(obj) == Contributor:
            return Contributor.objects\
                .filter(project__id=obj.project_id) \
                .filter(role="author") \
                .filter(user_id=request.user.pk).exists()
        if type(obj) == Project:
            return Contributor.objects\
                .filter(project__id=obj.pk) \
                .filter(role="author") \
                .filter(user_id=request.user.pk).exists()
        return obj.user == request.user


class IsContributor(BasePermission):

    def has_permission(self, request, view):
        requested_project = get_object_or_404(Project, pk=view.kwargs["pk"])
        allowed_user = request.user in requested_project.contributors.all()
        if request.user == requested_project.author or allowed_user:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
