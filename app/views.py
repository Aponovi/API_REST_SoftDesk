from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Project, Contributor, Issue, Comment
from app.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


class ProjectAPIView(APIView):

    def get(self, *args, **kwargs):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)


class ContributorAPIView(APIView):

    def get(self, *args, **kwargs):
        queryset = Contributor.objects.all()
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)


class IssueAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = Issue.objects.all()
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
