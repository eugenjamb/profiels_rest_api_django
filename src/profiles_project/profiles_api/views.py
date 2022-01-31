from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
            'Users HTTP methods as function (get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'api_view': an_apiview})

    def post(self, request):
        """create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating the object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handles updating the given object fields"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes the object"""

        return Response({'method': 'delete'})


class HelloViewSets(viewsets.ViewSet):
    """Test api view sets"""

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewSet': a_viewset})


