from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ShowSerializer, SetSerializer
from .models import Show, Set

class ShowView(generics.ListCreateAPIView):
    """This class defines the behavior of the show endpoint."""
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new show."""
        serializer.validated_data['author'] = self.request.user
        return super(ShowView, self).perform_create(serializer)

    def list(self, request):
        queryset = self.get_queryset().filter(author=request.user)
        serializer = ShowSerializer(queryset, many=True)
        return Response(serializer.data)
        

class SetView(generics.ListCreateAPIView):
    """This class defines the behavior of the set endpoint."""
    queryset = Set.objects.all()
    serializer_class = SetSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new set."""
        serializer.validated_data['author'] = self.request.user
        return super(SetView, self).perform_create(serializer)

    def list(self, request):
        queryset = self.get_queryset().filter(author=request.user)
        serializer = SetSerializer(queryset, many=True)
        return Response(serializer.data)