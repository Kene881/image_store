from django.shortcuts import render
from .models import ImagesTable
from rest_framework import viewsets
from .serializers import ImagesTableSerializer

# Create your views here.
class ImagesTableView(viewsets.ModelViewSet):
    queryset = ImagesTable.objects.all()
    serializer_class = ImagesTableSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.SessionAuthentication]