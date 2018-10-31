from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer,PollsSerializer
from rest_framework import viewsets
from .models import Polls

# Create your views here.
class HelloAPIView(APIView):
    """Testing API view"""
    serializer_class = HelloSerializer

    def get(self,request,format=None):
        """Returns a List of API views Features"""

        an_apiview = [
            'Uses HTTP methods as functions(get,post,patch,put,delete)',
            'It is similar to a traditional django view',
            'Gives you most control over your logic',
            'Its mapped  manually to URLs'
        ]
        return Response({
            'message':'Hello',
            'an_apiview':an_apiview
        })

    def post(self,request):
        """Create a  hello message from name."""
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating a project"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Patch request only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Deletes an object in the database"""
        return Response({'method':'delete'})

# viewsets starting from Here

class HelloViewset(viewsets.ViewSet):

    serializer_class = HelloSerializer

    def list(self,request):
        a_viewset = [
            'Uses HTTP methods as functions(get,post,patch,put,delete)',
            'It is similar to a traditional django view',
            'Gives you most control over your logic',
            'Its mapped  manually to URLs'
        ]

        return Response({
            'message':'Hello',
            'a_viewset':a_viewset
        })

    def create(self,request):
        """Create a new hello message"""

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handles getting an object by its ID."""
        return Response({'http_method':'GET'})

    def update(self,request,pk = None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles updating part of an object."""
        return Response({'http_method':'Patch'})

    def destroy(self,request,pk=None):
        """Handles removing an object"""
        return Response({'http_method':'Delete'})


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollsSerializer
    queryset = Polls.objects.all()