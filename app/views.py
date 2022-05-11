from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import Project
from app.serializers import ProjectSerializer


class ProjectAPIView(APIView):

    def get(self, *args, **kwargs):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
