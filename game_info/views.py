from rest_framework import viewsets
from .serializers import ServerSerializer
from .models import Server


class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
