from rest_framework.serializers import ModelSerializer

from app.models import Project, Contributor, Issue, Comment


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id',
                  'user',
                  "project",
                  "permission",
                  "role",
                  ]


class ProjectSerializer(ModelSerializer):
    user = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id',
                  "title",
                  "description",
                  "type",
                  "author_user",
                  "user"
                  ]


class IssueSerializer(ModelSerializer):
    model = Issue
    fields = ['id',
              'title',
              'description',
              'tag',
              'priority',
              'status',
              'author',
              'assignee',
              'created_time'
              ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "author",
            "issue",
            "created_time",
        ]
