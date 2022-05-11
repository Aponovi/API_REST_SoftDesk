from rest_framework.serializers import ModelSerializer

from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id',
                  "title",
                  "description",
                  "type",
                  "author_user",
                  ]
