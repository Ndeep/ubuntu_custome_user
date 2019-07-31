from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import FileSerializer
from .models import File


class FileView(viewsets.ModelViewSet):
    queryset=File.objects.all()
    serializer_class = FileSerializer

class PermissionView(APIView):
    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        obj=get_object_or_404(self.get_queryset(),pk=self.kwargs["pk"])
        self.check_object_permissions(self.request,obj)
        return obj


