from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer

from app.models import Project, Contributor, Issue, Comment
from authentication.models import User


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
        read_only__fields = ('project', 'role', 'id')


class ProjectSerializer(ModelSerializer):
    user = ContributorSerializer(source="users", read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_field_only = ['id', 'author']

    def create(self, validated_data):
        project = Project.objects.create(**validated_data)
        Contributor.objects.create(
            project_id=project.id,
            role="author",
            user_id=self.context["request"].user.id,
        )
        return project


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'status', 'created_time', 'id']
        optional_fields = ['assignee']
        read_only__fields = ['created_time', 'id', 'project']

    def create(self, validated_data):
        validated_data['author'] = self.context["request"].user
        validated_data['project'] = get_object_or_404(Project, pk=self.context["view"].kwargs.get('project_pk'))

        if 'assignee' not in validated_data:
            validated_data['assignee'] = validated_data['author']
        issue = Issue.objects.create(**validated_data)
        return issue


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description', 'id', 'author', 'issue', 'created_time']
        read_field_only = ['author', 'issue', 'created_time', 'id']

    def create(self, validated_data):
        validated_data['author'] = self.context["request"].user
        validated_data['issue'] = get_object_or_404(Issue, pk=self.context["view"].kwargs.get('issue_pk'))
        comment = Comment.objects.create(**validated_data)
        return comment
